
class ForwardChecking(object):
    
    def findSolution(self, variables):
        self.forwardChecking(0, variables)

    def forwardChecking(self, level, variables):
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

    # Returning True will halt the program - returning False allows it to continue 
    def problemSolved(self, level, pick, variables):
        for value in pick.domain:
            pick.value = value
            domainWipeout = False
            for queen in self.oneLeft(variables):
                if self.constraints.Wipeout(variables, queen):
                    domainWipeout = True
                    break
            if not domainWipeout:
                self.forwardChecking(level + 1, variables)

    def assignedValueLeadsToValidSolution(self, level, variables):
        return self.constraints.verify(variables) and self.backtracking(level + 1, variables)

    def oneLeft(variables):
        queensWithOneValueLeft = []
        for queen in variables.queens:
            if len(queen.domain) == 1:
                queensWithOneValueLeft.push(queen)
        return queensWithOneValueLeft