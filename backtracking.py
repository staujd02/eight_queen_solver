from constraints import Constraints

class BackTracking(object):

    def __init__(self):
        self.set = set()
        self.constraints = Constraints()

    def findSolution(self, variables):
        self.backtracking(0, variables)

    def backtracking(self, level, variables):
        pick = -1
        for idx, queen in enumerate(variables.queens):
            if queen.value == -1:
                pick = idx
                break

        if pick == -1:
            return True
        
        for value in variables.queens[pick].domain:
            variables.queens[pick].value = value
            if self.constraints.verify(variables):
                if self.backtracking(level + 1, variables):
                    return True
        variables.queens[pick].value = -1
        return False