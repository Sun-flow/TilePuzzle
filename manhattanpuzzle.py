
from copy import deepcopy

def manhattanpuzzle(start, goal, size):
    path = stateSearch([start], goal, [], 1, size)

    for x in path:
        print(x) 

def stateSearch(unexplored, goal, path, depth, size):

    print(
    #    'unexplored = ', unexplored,
        '\npath = ', path
    )

    if unexplored == [] or depth > 11:
        return []
    
    dist = 99999
    whichBoard = 0

    for x in range(len(unexplored)):
        
        if len(path) > 2 and path[-2] == unexplored[x]:
                print(
                        'unexplored[', x, '] = ', unexplored[x],
                        '\npath[-1] = ', path[-1],
                        '\npath[-2] = ', path[-2],
                    )

                print('repeat')
        else:
            print('found shorter')
            curr = findManhattan(unexplored[x], goal, size)

            if curr < dist:
                dist = curr
                whichBoard = x

    if goal == unexplored[whichBoard]:
        return path + [goal]
    else:    
        return stateSearch(findChildren(unexplored[whichBoard], size), goal, path + [unexplored[whichBoard]], depth + 1, size)


def findManhattan(board, goal, size):
    manDist = 0
    for x in range(size):
        for y in range(size):
            tileLoc = findTile(board[x][y], goal, size)
            manDist += abs(tileLoc[0] - x) + abs(tileLoc[1] - y)

    return manDist


def findTile(num, goal, size):
    for x in range(size):
        for y in range(size):
            if goal[x][y] == num:
                return [x, y]


def findChildren(board, size):
    newStates = []
    left = generateLeftMove(board, size)
    if left != None:
        newStates += [left]

    right = generateRightMove(board, size)    
    if right != None:
        newStates += [right]

    up = generateUpMove(board, size)    
    if up != None:
        newStates += [up]

    down = generateDownMove(board, size)
    if down  != None:
        newStates += [down]
    return newStates



def generateLeftMove(currState, size):
    localState = deepcopy(currState)
    for x in range(size):
        for y in range(1, size):
            if localState[x][y] == 0:
                left = localState[x][y - 1]
                localState[x][y] = left
                localState[x][y - 1] = 0
                return localState


def generateRightMove(currState, size):
    localState = deepcopy(currState)
    for x in range(size):
        for y in range(size - 1):
            if localState[x][y] == 0:
                right = localState[x][y + 1]
                localState[x][y] = right
                localState[x][y + 1] = 0
                return localState


def generateUpMove(currState, size):
    localState = deepcopy(currState)
    for x in range(1, size):
        for y in range(size):
            if localState[x][y] == 0:
                up = localState[x - 1][y]
                localState[x][y] = up
                localState[x - 1][y] = 0
                return localState


def generateDownMove(currState, size):
    localState = deepcopy(currState)
    for x in range(2):
        for y in range(3):
            if localState[x][y] == 0:
                down = localState[x + 1][y]
                localState[x][y] = down
                localState[x + 1][y] = 0
                return localState