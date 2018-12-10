from arc_consistentcy import ArcConsistency

class GlobalArcConsistency(object):

    def __init__(self, constraints):
        self.ac = ArcConsistency(constraints)
        self.constraints = constraints
    
    def findSolution(self, variables):
        self.gac(0, variables)
    
    def gac(self, level, variables):
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
    
    def problemSolved(self, level, pick, variables):
        # Prune all values of X != v from CurDom[X]
        # for each constraint C whose scope contains X
        # Put C on GACQueue
        # if(GAC_Enforce() != DWO)
        # GAC(Level+1) /*all constraints were ok*/
        # RestoreAllValuesPrunedFromCurDoms()
        for value in pick.domain:
            pick.value = value
            if self.ac.arcConsistent(variables, pick):
                if self.gac(level + 1, variables):
                    return True
                self.ac.restore(variables, pick)
        pick.value = -1

    def assignedValueLeadsToValidSolution(self, level, variables):
        return self.constraints.verify(variables) and self.backtracking(level + 1, variables)

    def oneLeft(self, variables):
        queensWithOneValueLeft = []
        for queen in variables.queens:
            if len(queen.domain) == 1:
                queensWithOneValueLeft.push(queen)
        return queensWithOneValueLeft