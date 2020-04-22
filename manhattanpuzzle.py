
from copy import deepcopy

def manhattanpuzzle(start, goal, size):
    path = stateSearch([start], goal, [], 1, size)

    for x in path:
        for y in x:
            print(y) 
        print('\n')

    print('Path length = ', len(path))

def stateSearch(unexplored, goal, path, depth, size):
    if unexplored == [] or depth > 20:
        return []
    
    
    curr = []
    for x in range(len(unexplored)):
        if not isRepeat(unexplored[x], path):            
            curr.append((x, findManhattan(unexplored[x], goal, size)))

    boards = sortBoards(curr)

    for x in range(len(boards)):
        currBoard = unexplored[boards[x][0]]
        if goal == currBoard:
            return path + [goal]
        
        result = stateSearch(findChildren(currBoard, size),goal, path + [currBoard], depth + 1, size)

        if result != []:
            return result
    
    return []


def isRepeat(currBoard, path):
    if len(path) > 1 and (path[-2] == currBoard or path[-1] == currBoard):
        return True
    else:
        return False



def sortBoards(arr):
    for x in range(len(arr)):
        for y in range(0, len(arr)-x-1):
            if arr[y][1] > arr[y+1][1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    
    return arr




def findManhattan(board, goal, size):
    manDist = 0
    for x in range(size):
        for y in range(size):
            tileLoc = findTile(board[x][y], goal, size)
            manDist += abs(tileLoc[0] - x) + abs(tileLoc[1] - y)

    return manDist


def findTile(num, board, size):
    for x in range(size):
        for y in range(size):
            if board[x][y] == num:
                return [x, y]


def findChildren(board, size):
    newStates = []
    emptyTile = findTile(0, board, size)
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


#TODO: apply empty tile knowledge, eliminate searches
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