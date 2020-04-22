
from copy import deepcopy

def manhattanpuzzle(start, goal, size):
    path = stateSearch([start], goal, [], 1, size)

    for x in path:
        for y in x:
            print(y) 
        print('\n')

    print('Path length = ', len(path))

def stateSearch(unexplored, goal, path, depth, size):

    print(
    #    'unexplored = ', unexplored,
        '\npath = ', path
    )

    if unexplored == [] or depth > 20:
        return []
    
    
    curr = []
    for x in range(len(unexplored)):
        if not isRepeat(unexplored[x], path):            
            curr.append((x, findManhattan(unexplored[x], goal, size)))

    boards = sortBoards(curr)

    print(
        'boards = ', boards
    )

    for x in range(len(boards)):
        print(
            'board ', x + 1,
            ' in range ', len(boards),
            '\n', boards
        )
        currBoard = unexplored[boards[x][0]]
        if goal == currBoard:
            return path + [goal]
        
        result = stateSearch(findChildren(currBoard, size),goal, path + [currBoard], depth + 1, size)

        if result != []:
            return result
    
    return []


def isRepeat(currBoard, path):

    if len(path) > 0 and path[-1] == currBoard:
        print(
                'repeat:\n'
                'currboard = ', currBoard,
                '\npath[-1] = ', path[-1],
                '\n path len = ', len(path)
        )
        return True
    elif len(path) > 1 and (path[-2] == currBoard or path[-1] == currBoard):
        print(
            'repeat:\n'
            'currboard = ', currBoard,
            '\npath[-2] = ', path[-2],
            '\n path len = ', len(path)
        )
        return True
    elif len(path) > 2 and (path[-2] == currBoard or path[-1] == currBoard or path[-3] == currBoard):
        print(
            'repeat:\n'
            'currboard = ', currBoard,
            '\npath[-3] = ', path[-3],
            '\n path len = ', len(path)
        )
        return True
    elif len(path) > 3 and (path[-2] == currBoard or path[-1] == currBoard or path[-3] == currBoard or path[-4] == currBoard):
        print(
            'repeat:\n'
            'currboard = ', currBoard,
            '\npath[-4] = ', path[-4],
            '\n path len = ', len(path)
        )
        return True
    else:
        return False



def sortBoards(arr):
    print(
        'Tuple Array: ', arr
    )
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