from constraints import Constraints

class BackTracking(object):

    def __init__(self):
        self.constraints = Constraints()

    def findSolution(self, variables):
        self.backtracking(0, variables)

    def backtracking(self, level, variables):
        selectedQueen = self.pickUnassignedQueenFrom(variables)
        if selectedQueen == None:
            return True
        if self.problemSolved(level, selectedQueen, variables):
            return True
        selectedQueen.value = -1
        return False
    
    def pickUnassignedQueenFrom(self, variables):
        for idx, queen in enumerate(variables.queens):
            if queen.value == -1:
                return queen
        return None 
    
    def problemSolved(self, level, pick, variables):
        for value in pick.domain:
            pick.value = value
            if self.assignedValueLeadsToValidSolution(level, variables):
                return True
        return False

    def assignedValueLeadsToValidSolution(self, level, variables):
        return self.constraints.verify(variables) and self.backtracking(level + 1, variables)
