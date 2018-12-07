
class BetterConstraints(object):

    def __init__(self, numberOfQueens):
        self.populateConstraints(numberOfQueens)

    def populateConstraints(self,numberOfQueens):
        self.rows = set(range(1, numberOfQueens + 1))
        self.negativeDiagonals = set(range(-1 * (numberOfQueens - 1), numberOfQueens))
        self.positiveDiagonals = set(range(2, 2*numberOfQueens + 1))

    # def rowViolatesConstraint(self, variables, queen1, queen2):
    #     return self.bothQueensHaveAValue(queen1, queen2) and queen1.value == queen2.value

    # def diagonalViolatesConstraint(self, variables, queen1, queen2):
    #     return self.bothQueensHaveAValue(queen1, queen2) and abs(queen1.value - queen2.value) == abs(queen1.number - queen2.number)

    # def bothQueensHaveAValue(self, queen1, queen2):
    #     return not queen1.unassigned() and not queen2.unassigned()

    # def queenAppearsInConstraintScope(self, variables, queen, constraint):
    #     queen1 = variables.queens[constraint[1] - 1]
    #     queen2 = variables.queens[constraint[0] - 1]
    #     return queen1.number == queen.number and not queen2.number == queen.number

    # def obtainQueenToCheckForDomain(self, variables, constraint, queen):
    #     queenToCheck = -1
    #     queen1 = variables.queens[constraint[1] - 1]
    #     queen2 = variables.queens[constraint[0] - 1]
    #     if not queen1.number == queen.number and not queen2.number == queen.number or not queen1.unassigned() and not queen2.unassigned():
    #         return None
    #     if queen2.number == queen.number:
    #         return queen1
    #     if queen1.number == queen.number:
    #         queenToCheck = queen2

    # def domainValuesToRemove(self, variables, constraint, queenToCheck, removed):
    #     remove = set()
    #     for value in queenToCheck.domain:
    #         queenToCheck.value = value
    #         if self.constraintFails(variables, constraint):
    #             remove.add(value)
    #             removed.append((queenToCheck.number - 1, value))
    #     return remove

    def copySets(self, variables):
        return (self.rows.copy(), self.negativeDiagonals.copy(), self.positiveDiagonals.copy())
    
    def setRemoval(self, sets, queen):
        if queen.value == -1:
            return
        sets[0].remove(queen.value)
        sets[1].remove(queen.value - queen.number)
        sets[2].remove(queen.value + queen.number)

    def rectifySets(self, variables, sets):
        for queen in variables.queens:
            self.setRemoval(sets, queen)

    def setCheck(self, variables):
        copySet = self.copySets(variables)
        try:
            self.rectifySets(variables, copySet)
        except KeyError: 
            return None
        return copySet
    
    def wipeout(self, variables):
        result = self.setCheck(variables)
        if result == None:
            return False
        self.rows = result[0]
        self.negativeDiagonals = result[1]
        self.positiveDiagonals = result[2]
        return True

    # def wipeout(self, variables, queen):
    #     removed = []
    #     for constraint in self.set:
    #         queenToCheck = self.obtainQueenToCheckForDomain(
    #             variables, constraint, queen)
    #         if queenToCheck == None:
    #             continue
    #         remove = self.domainValuesToRemove(
    #             variables, constraint, queenToCheck, removed)
    #         if len(queenToCheck.domain) == len(remove):
    #             self.restore(variables, removed)
    #             queenToCheck.value = -1
    #             return None
    #         queenToCheck.domain = queenToCheck.domain.difference(remove)
    #         queenToCheck.value = -1
    #     return removed

    def verify(self, variables):
        result = self.setCheck(variables)
        if result == None:
            return False
        return True

    # def constraintFails(self, variables, constraint):
    #     return constraint[2](variables, variables.queens[constraint[0] - 1], variables.queens[constraint[1] - 1])

    # def restore(self, variables, domainTuples):
    #     for indexValuePair in domainTuples:
    #         variables.queens[indexValuePair[0]].domain.add(indexValuePair[1])
