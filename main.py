import random
import time
import timeit

from forwardchecking import ForwardChecking
from backtracking import BackTracking
from variables import Variables
from modified_constraints import ModifiedConstraints
from arc_consistentcy import ArcConsistency
from arcs import Arcs

ct = ModifiedConstraints(8)
problem = Variables(8)

ac = ArcConsistency(Arcs(8))
print(ac.arcConsistent(problem))


# problem.queens.value = 

# problem.queens[4].domain = set([5])

# forwardchecking = ForwardChecking(ct)
# forwardchecking.findSolution(problem)

# for idx, queen in enumerate(problem.queens):
#     print("Queen " + str(idx + 1) + ": " + str(queen.value))

# def runBackTracking(numberOfQueens):
#     ct = ModifiedConstraints(numberOfQueens)
#     problem = Variables(numberOfQueens)
#     bt = BackTracking(ct)
#     bt.findSolution(problem)

# def runForwardChecking(numberOfQueens):
#     ct = ModifiedConstraints(numberOfQueens)
#     problem = Variables(numberOfQueens)
#     fc = ForwardChecking(ct)
#     fc.findSolution(problem)

# def prepTest(numberOfQueens, style):
#     if style == 1:
#         return lambda: runBackTracking(numberOfQueens)
#     else:
#         return lambda: runForwardChecking(numberOfQueens)

# start = 15 
# random.seed(time.time())

# def trash(): return None

# print("       | Back-Tracking | Forward-Checking |")
# for x in range(4, start):
#     btTest = prepTest(x, 1)
#     fcTest = prepTest(x, 0)
#     btTime = timeit.timeit(btTest, trash, time.time, 1)
#     fcTime = timeit.timeit(fcTest, trash, time.time, 1)
#     btTime = 0
#     print("Size " + str(x) + ": " + str(btTime) + ", " + str(fcTime))