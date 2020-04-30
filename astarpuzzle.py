from copy import deepcopy
from queue import PriorityQueue
import manhattanpuzzle


def toTup(inList):
    tupArr = []
    for row in inList:
        tupArr += [tuple(row)]

    return tuple(tupArr)


#TODO: Implement non-square board sizes (use a tuple for x and y size)

def astarpuzzle(start, goal):
    size = (len(start), len(start[0]))
    emptyTile = manhattanpuzzle.findTile(0, start, size)
    board = (start, emptyTile)
    output = stateSearch(start, goal, board, 1, size)
    cameFrom = output[0]
    moves = output[1]
    states = output[2]
    generated = output[3]

    currBoard = (toTup(goal))
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
    print('# of moves: ', moves)
    print('# of states explored: ', states)
    print('# of states generated: ', generated)

def stateSearch(startBoard, goal, path, depth, size):
    open = PriorityQueue()
    goalTup = toTup(goal)
    dist = manhattanpuzzle.findmanhattan(startBoard, goal, size)
    open.put((dist, 0, startBoard))
    cameFrom = {toTup(startBoard) : None}
    moves = {toTup(startBoard) : 0}

    states = 0
    generated = 0
    while not open.empty():
        currBoard = open.get()
        states += 1
        for child in manhattanpuzzle.findChildren(currBoard[2], size):
            generated += 1
            childTup = toTup(child)
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
                
                return (cameFrom, moves[childTup], states, generated)
            

        





