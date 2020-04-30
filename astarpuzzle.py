from copy import deepcopy
from queue import PriorityQueue
import manhattanpuzzle


def toTup(list):
    return (tuple(list[0]), tuple(list[1]), tuple(list[2]))


def astarpuzzle(start, goal):
    size = len(start)
    emptyTile = manhattanpuzzle.findTile(0, start, size)
    board = (start, emptyTile)
    cameFrom = stateSearch(start, goal, board, 1, size)

    currBoard = (tuple(goal[0]), tuple(goal[1]), tuple(goal[2]))
    path = [goal]
    while cameFrom[currBoard] != None:
        path += [cameFrom[currBoard]]
        nextBoard = cameFrom[currBoard]
        currBoard = toTup(nextBoard)

    flipPath = path[::-1]
    for board in flipPath:
        print()
        for row in board:
            print(row)
    print('Path length = ', len(flipPath))

def stateSearch(startBoard, goal, path, depth, size):
    open = PriorityQueue()
    goalTup = (tuple(goal[0]), tuple(goal[1]), tuple(goal[2]))
    dist = manhattanpuzzle.findmanhattan(startBoard, goal, size)
    open.put((dist, 0, startBoard))
    cameFrom = {(tuple(startBoard[0]), tuple(startBoard[1]), tuple(startBoard[2])) : None}
    moves = {(tuple(startBoard[0]), tuple(startBoard[1]), tuple(startBoard[2])) : 0}

    while not open.empty():
        currBoard = open.get()
        for child in manhattanpuzzle.findChildren(currBoard[2], size):
            childTup = (tuple(child[0]), tuple(child[1]), tuple(child[2]))
            if childTup not in cameFrom:
                dist = currBoard[1] + manhattanpuzzle.findmanhattan(childTup, goal, size) + 1
                open.put((dist, currBoard[1]+1, child))
                cameFrom[childTup] = currBoard[2]
                moves[childTup] = currBoard[1]+1
            else:
                if currBoard[1]+1 < moves[childTup]:
                    moves[childTup] = currBoard[1]+1
                    cameFrom[childTup] = currBoard[2]

            if goalTup == childTup:
                return cameFrom
            

        





