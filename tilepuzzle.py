from copy import deepcopy

def tilePuzzle(start, goal):
    return reverse(stateSearch([start], goal, [], 1))

def stateSearch(unexplored, goal, path, depth):
    if unexplored == [] or depth > 30:
        return []
    elif goal == head(unexplored):
        return cons(goal, path)

    #Check to ensure that path is not simply swapping between 2 configurations over and over again, save memory + recursions (yeah I know it's basically a heuristic but... I wanted to be able to tell if my program was actually solving anything at all in order to debug it)
    elif len(path) > 1 and head(unexplored) == path[1]:
        return stateSearch(tail(unexplored), goal, path, depth + 1)

    else:
        result = stateSearch(generateNewStates(head(unexplored)), goal, cons(head(unexplored), path), depth + 1)
        
        if result != []:
            return result

        else:
            return stateSearch(tail(unexplored), goal, path, depth + 1)



#Directional Movement cases. Each case leaves off one of the rows or columns, based on where moves of its particular direction would not be valid. Deep copy is used so as not to modify default state.
def generateLeftMove(currState):
    localState = deepcopy(currState)
    for x in range(3):
        for y in range(1, 3):
            if localState[x][y] == 0:
                left = localState[x][y - 1]
                localState[x][y] = left
                localState[x][y - 1] = 0
                return localState


def generateRightMove(currState):
    localState = deepcopy(currState)
    for x in range(3):
        for y in range(2):
            if localState[x][y] == 0:
                right = localState[x][y + 1]
                localState[x][y] = right
                localState[x][y + 1] = 0
                return localState


def generateUpMove(currState):
    localState = deepcopy(currState)
    for x in range(1, 3):
        for y in range(3):
            if localState[x][y] == 0:
                up = localState[x - 1][y]
                localState[x][y] = up
                localState[x - 1][y] = 0
                return localState


def generateDownMove(currState):
    localState = deepcopy(currState)
    for x in range(2):
        for y in range(3):
            if localState[x][y] == 0:
                down = localState[x + 1][y]
                localState[x][y] = down
                localState[x + 1][y] = 0
                return localState




#Generate states. Avoids adding a blank state to the set, as it screws up later processing. Unfortunate use of checks and memory allocation, but functional.
def generateNewStates(currState):
    newStates = []
    left = generateLeftMove(currState)
    if left != None:
        newStates += [left]

    right = generateRightMove(currState)    
    if right != None:
        newStates += [right]

    up = generateUpMove(currState)    
    if up != None:
        newStates += [up]

    down = generateDownMove(currState)
    if down  != None:
        newStates += [down]
    return newStates




#Given functional programming functions. No changes.
def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst