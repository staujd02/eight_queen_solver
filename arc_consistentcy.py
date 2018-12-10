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

    def arcConsistent(self, variables, lastAssignedQueen = None):
        self.initFill()
        for queen in variables.queens:
            if queen.value != -1:
                queen.domain = set([queen.value])
        while self.queue.qsize() != 0:
            c = self.queue.get()
            if self.revise(variables, c):
                if len(variables.queens[c[0] - 1].domain) == 0:
                    self.restore(variables, lastAssignedQueen)
                    return False
                for arc in self.constraints.set:
                    if arc[0] == c[0] and arc[1] != c[1]:
                        self.queue.put(arc)
        return True

    def revise(self, variables, arc):
        revised = False
        queenInQuestion = variables.queens[arc[0] - 1]
        trimmedValues = set()
        currentValue = queenInQuestion.value
        for value in queenInQuestion.domain:
            queenInQuestion.value = value
            if self.constraintUnsatisfiable(variables, arc):
                trimmedValues.add(value)
                revised = True
        queenInQuestion.value = currentValue
        queenInQuestion.domain = queenInQuestion.domain.difference(trimmedValues)
        return revised
    
    def constraintUnsatisfiable(self, variables, arc):
        unsatisfiable = True
        queenToCheckAgainst = variables.queens[arc[1] - 1]
        currentValue = queenToCheckAgainst.value
        for value in queenToCheckAgainst.domain:
            queenToCheckAgainst.value = value
            if self.constraints.verify(variables):
                unsatisfiable = False
                break
        queenToCheckAgainst.value = currentValue
        return unsatisfiable

    def restore(self, variables, lastAssignedQueen):
        for q in variables.queens:
            q.domain = set(range(1, len(variables.queens) + 1))
        if lastAssignedQueen != None:
            lastAssignedQueen.value = -1
            self.arcConsistent(variables)