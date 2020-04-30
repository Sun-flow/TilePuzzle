# TilePuzzle

Sorting algorithms for 3x3 and 4x4 tile puzzles.

tilepuzzle.py is a dumb solver with no heuristics, will likely not solve puzzles greater than 3x3. Completed for a class assignment as an intro to python for AI.

manhattanpuzzle.py is a personal project extension of this assignment, where I implement a manhattan distance heuristic. 
This puzzle solver does well with 3x3 and okay with 4x4, but is not guaranteed to solve for best path.

astarpuzzle.py implements A* to solve tilepuzzles. Guarantees fastest path. Does well with 3x3 and 4x4, robust enough to handle larger boards and boards with uneven dimensions. Time complexity on larger boards is not great.