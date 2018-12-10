import Queue

class ArcConsistency(object):
    
    def __init__(self, constraints):
        self.constraints = constraints
        self.queue = Queue.Queue(maxsize=200)

    def initFill(self):
        while not self.queue.empty():
            self.queue.get()
        for c in self.constraints.set:
            self.queue.put(c)

    def arcConsistent(self, variables):
        self.initFill()
        for queen in variables.queens:
            if queen.value != -1:
                queen.domain = set([queen.value])
        while self.queue.qsize() != 0:
            c = self.queue.get()
            print("Queue Lenght: " + str(self.queue.qsize()))
            if self.revise(variables, c):
                if len(variables.queens[c[0] - 1].domain) == 0:
                    return False
                for arc in self.constraints.set:
                    if arc[0] == c[0] and arc[1] != c[1]:
                        self.queue.put(arc)
        return True

    def revise(self, variables, arc):
        revised = False
        queenInQuestion = variables.queens[arc[0] - 1]
        trimmedValues = set()
        for value in queenInQuestion.domain:
            queenInQuestion.value = value
            if self.constraintUnsatisfiable(variables, arc):
                trimmedValues.add(value)
                revised = True
            queenInQuestion.value = -1
        queenInQuestion.domain = queenInQuestion.domain.difference(trimmedValues)
        return revised
    
    def constraintUnsatisfiable(self, variables, arc):
        unsatisfiable = True
        queenToCheckAgainst = variables.queens[arc[1] - 1]
        for value in queenToCheckAgainst.domain:
            queenToCheckAgainst.value = value
            if self.constraints.verify(variables):
                unsatisfiable = False
                break
        queenToCheckAgainst.value = -1
        return unsatisfiable

    # def findSolution(self, variables):
    #     self.backtracking(0, variables)

    # def backtracking(self, level, variables):
    #     selectedQueen = self.pickUnassignedQueenFrom(variables)
    #     if selectedQueen == None:
    #         return True
    #     if self.problemSolved(level, selectedQueen, variables):
    #         return True
    #     selectedQueen.value = -1
    #     return False
    
    # def pickUnassignedQueenFrom(self, variables):
    #     for idx, queen in enumerate(variables.queens):
    #         if queen.value == -1:
    #             return queen
    #     return None 
    
    # def problemSolved(self, level, pick, variables):
    #     for value in pick.domain:
    #         pick.value = value
    #         if self.assignedValueLeadsToValidSolution(level, variables):
    #             return True
    #     return False

    # def assignedValueLeadsToValidSolution(self, level, variables):
    #     return self.constraints.verify(variables) and self.backtracking(level + 1, variables)