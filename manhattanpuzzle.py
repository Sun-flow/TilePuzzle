
from copy import deepcopy

def manhattanpuzzle(start, goal):
    size = (len(start), len(start[0]))
    emptyTile = findTile(0, start, size)
    board = (start, emptyTile)
    path = stateSearch(board, goal, [board[0]], 1, size)

    for x in path:
        for y in x:
            print(y) 
        print('\n')

    print('Path length = ', len(path))

def stateSearch(unexplored, goal, path, depth, size):
    if depth > 25:
        return []
    elif goal == unexplored[0]:
        return path
    children = findChildren(unexplored, size)
    curr = []
    for x in range(len(children)):
        if not isRepeat(children[x][0], path):            
            curr.append((x, findmanhattan(children[x][0], goal, size)))

    boards = sortBoards(curr)

    for x in range(len(boards)):
        currBoard = children[boards[x][0]]
        if goal == currBoard[0]:
            return path + [goal]
        
        result = stateSearch(currBoard, goal, path + [currBoard[0]], depth + 1, size)

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


#Return distance of each individual tile to its goal space (innefficient method, time complexity n)
def findmanhattan(board, goal, size):
    manDist = 0
    for x in range(size[0]):
        for y in range(size[1]):
            tileLoc = findTile(board[x][y], goal, size)
            manDist += abs(tileLoc[0] - x) + abs(tileLoc[1] - y)

    return manDist

#Find a certain number on the board, return it's (x,y) coordinates. Only used to find empty square during tile generation to reduce searching. 
def findTile(num, board, size):
    for x in range(size[0]):
        for y in range(size[1]):
            if board[x][y] == num:
                return (x, y)

#Generate children of input board (max 4, cardinal directions)
def findChildren(board, size):
    emptyTile = findTile(0, board, size)
    newStates = []
    x = emptyTile[0]
    y = emptyTile[1]
    if y > 0:
        left = generateLeftMove(board, size, emptyTile)
        if left != None:
            newStates += [left]

    if y < size[1] - 1:
        right = generateRightMove(board, size, emptyTile)    
        if right != None:
            newStates += [right]

    if x > 0:
        up = generateUpMove(board, size, emptyTile)    
        if up != None:
            newStates += [up]

    if x < size[0] - 1:
        down = generateDownMove(board, size, emptyTile)
        if down  != None:
            newStates += [down]
    return newStates


def generateLeftMove(currState, size, emptyTile):
    localState = deepcopy(currState)
    x = emptyTile[0]
    y = emptyTile[1]
    if y > 0:
        if localState[x][y] == 0:
            left = localState[x][y - 1]
            localState[x][y] = left
            localState[x][y - 1] = 0
            return localState


def generateRightMove(currState, size, emptyTile):
    localState = deepcopy(currState)
    x = emptyTile[0]
    y = emptyTile[1]
    if y < size[1] - 1:
        if localState[x][y] == 0:
            right = localState[x][y + 1]
            localState[x][y] = right
            localState[x][y + 1] = 0
            return localState         


def generateUpMove(currState, size, emptyTile):
    localState = deepcopy(currState)
    x = emptyTile[0]
    y = emptyTile[1]
    if x > 0:
        if localState[x][y] == 0:
            up = localState[x - 1][y]
            localState[x][y] = up
            localState[x - 1][y] = 0
            return localState
            


def generateDownMove(currState, size, emptyTile):
    localState = deepcopy(currState)
    x = emptyTile[0]
    y = emptyTile[1]
    if x < size[0] - 1:
        if localState[x][y] == 0:
            down = localState[x + 1][y]
            localState[x][y] = down
            localState[x + 1][y] = 0
            return localState