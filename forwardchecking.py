
from constraints import Constraints

class ForwardChecking(object):
    
    def __init__(self, constraints):
        self.constraints = constraints
    
    def findSolution(self, variables):
        self.forwardChecking(0, variables)

    def forwardChecking(self, level, variables):
        selectedQueen = self.pickUnassignedQueenFrom(variables)
        if selectedQueen == None:
            return True
        if self.problemSolved(level, selectedQueen, variables):
            return True
        return False
    
    def pickUnassignedQueenFrom(self, variables):
        for idx, queen in enumerate(variables.queens):
            if queen.value == -1:
                return queen
        return None 

    # Returning True will halt the program - returning False allows it to continue 
    def problemSolved(self, level, pick, variables):
        for value in pick.domain:
            pick.value = value
            domainWipeout = False
            removedDomains = self.constraints.wipeout(variables, pick)
            if removedDomains == None:
                domainWipeout = True
            if not domainWipeout:
                if self.forwardChecking(level + 1, variables):
                    return True
                self.constraints.restore(variables, removedDomains)
        pick.value = -1

    def assignedValueLeadsToValidSolution(self, level, variables):
        return self.constraints.verify(variables) and self.backtracking(level + 1, variables)

    def oneLeft(self, variables):
        queensWithOneValueLeft = []
        for queen in variables.queens:
            if len(queen.domain) == 1:
                queensWithOneValueLeft.push(queen)
        return queensWithOneValueLeft