from copy import deepcopy
from queue import PriorityQueue
import manhattanpuzzle

#Function to turn 2D lists into tuples for compatibility with dictionaries
#!ATTENTION! Hi Professor, this method is actually the method I have the biggest question about. 
# I'm not sure what the cost of this conversion to tuples looks like, or its time complexity. 
# I imagined that unordered maps (dictionaries) from my C++ knowledge would be the best way to store BFS data,
# but due to my unfamiliarity with Python I am worried that I am making things needlessly complicated for myself.
# I'm hoping you could give me feedback on this method before I carry it out on our more complicated HW2.
# This method will work I'm sure, but I would rather program efficient code as much as possible.
# 
# Thank you!      
def toTup(inList):
    tupArr = []
    for row in inList:
        tupArr += [tuple(row)]

    return tuple(tupArr)


#TODO: Implement non-square board sizes (use a tuple for x and y size)

def astarpuzzle(start, goal):

    #Gather characteristics of input board for easier
    size = (len(start), len(start[0]))

    #Save search output into list, split into named variables for easier use
    output = stateSearch(start, goal, [start], 1, size)
    cameFrom = output[0] #Dictionary {someBoard : prevBoard}, used to backtrace path
    moves = output[1] #Dictionary {Board : moves to get to board}
    states = output[2] #Counter for number of states explored
    generated = output[3] #Counter for number of states generated


    #Retrace path from goal to start, then reverse the path. This seems costly and clunky to me.
    currBoard = (toTup(goal))
    path = [goal]
    while cameFrom[currBoard] != None:
        path += [cameFrom[currBoard]]
        nextBoard = cameFrom[currBoard]
        currBoard = toTup(nextBoard)
    flipPath = path[::-1]

    #Print path out, along with other data saved above
    for board in flipPath:
        print()
        for row in board:
            print(row)
    print('\nPath length = ', len(flipPath))
    print('# of moves: ', moves)
    print('# of states explored: ', states)
    print('# of states generated: ', generated)



def stateSearch(startBoard, goal, path, depth, size):

    #Prepare starting data point and containers for BFS
    open = PriorityQueue()
    goalTup = toTup(goal)
    dist = manhattanpuzzle.findmanhattan(startBoard, goal, size)

    #Data in array follows form of (A* distance for someBoard, moves taken to get to this someBoard, someBoard)
    open.put((dist, 0, startBoard))
    cameFrom = {toTup(startBoard) : None}
    moves = {toTup(startBoard) : 0}

    states = 0
    generated = 0
    while not open.empty():
        currNode = open.get()

        #Necessary data for manipulation, saved in intelligible variable
        #currDist = currNode[0]
        currMoves = currNode[1]
        currBoard = currNode[2]        

        states += 1

        #Search through all children of currBoard, add any new board states to open and change cameFrom + moves for any repeats with a faster path
        for child in manhattanpuzzle.findChildren(currBoard, size):
            generated += 1
            childTup = toTup(child)
            if childTup not in cameFrom:
                dist = currMoves + manhattanpuzzle.findmanhattan(childTup, goal, size) + 1
                open.put((dist, currMoves+1, child))
                cameFrom[childTup] = currBoard
                moves[childTup] = currMoves+1
            else:
                if currMoves+1 < moves[childTup]:
                    moves[childTup] = currMoves+1
                    cameFrom[childTup] = currBoard

            if goalTup == childTup:
                
                return (cameFrom, moves[childTup], states, generated)
            

        





