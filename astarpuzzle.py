from copy import deepcopy
from queue import PriorityQueue
import manhattanpuzzle



def astarpuzzle(start, goal):
    size = len(start)
    emptyTile = manhattanpuzzle.findTile(0, start, size)
    board = (start, emptyTile)
    cameFrom = stateSearch(start, goal, board, 1, size)

    currBoard = goal
    path = [goal]
    while cameFrom[currBoard] != None:
        path += cameFrom[currBoard]
        nextBoard = cameFrom[currBoard]
        currBoard = nextBoard


    print('Path length = ', len(path))

def stateSearch(startBoard, goal, path, depth, size):
    open = PriorityQueue()

    dist = manhattanpuzzle.findmanhattan(startBoard, goal, size)
    open.put((dist, 0, startBoard))
    cameFrom = {tuple(tuple(startBoard)) : None}
    moves = {tuple(tuple(startBoard)) : 0}

    print(startBoard)

    while not open.empty():
        currBoard = open.get()
        for child in manhattanpuzzle.findChildren(currBoard[2], size):
            print(child)
            if tuple(child) not in cameFrom:
                dist = currBoard[1] + manhattanpuzzle.findmanhattan(tuple(child), goal, size) + 1
                open.put(dist, currBoard[1]+1, child)
                cameFrom[tuple(child)] = currBoard[2]
                moves[tuple(child)] = currBoard[1]+1
            else:
                if currBoard[1]+1 < moves[child]:
                    moves[child[0]] = currBoard[1]+1
                    cameFrom[child[0]] = currBoard[2]

            if goal == child[0]:
                return cameFrom
            

        





