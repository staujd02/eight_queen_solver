
from backtracking import BackTracking
from variables import Variables

bt = BackTracking()

problem = Variables(8)
problem.queens[4].value = 5
bt.findSolution(problem)

for idx, queen in enumerate(problem.queens):
    print("Queen " + str(idx + 1) + ": " + str(queen.value))