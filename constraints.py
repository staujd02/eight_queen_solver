
class Constraints(object):

    def __init__(self, numberOfQueens):
        self.set = set()
        self.populateConstraints(self.set, numberOfQueens)

    def populateConstraints(self, mySet, numberOfQueens):
        self.rowConstraints(mySet, numberOfQueens)
        self.diagonalConstraints(mySet, numberOfQueens)

    def rowConstraints(self, set, numberOfQueens):
        for x in range(1, numberOfQueens):
            for y in range(x + 1, numberOfQueens + 1):
                set.add((x, y, lambda variables, queen1, queen2: self.rowViolatesConstraint(variables, queen1, queen2)))

    def rowViolatesConstraint(self, variables, queen1, queen2):
        return queen1.value != -1 and queen2.value != -1 and queen1.value == queen2.value

    def diagonalConstraints(self, set, numberOfQueens):
        for x in range(1, numberOfQueens):
            for y in range(x + 1, numberOfQueens + 1):
                set.add((x, y, lambda variables, queen1, queen2: self.diagonalViolatesConstraint(variables, queen1, queen2)))

    def diagonalViolatesConstraint(self, variables, queen1, queen2):
        return queen1.value != -1 and queen2.value != -1 and abs(queen1.value - queen2.value) == abs(variables.queens.index(queen1) - variables.queens.index(queen2))

    def queensRowsConflict(self, variables):
        availableRows = set(range(1,len(variables.queens) + 1))
        for queen in variables.queens:
            if not queen.unassigned():
                availableRows.remove(queen.value)

    def validRows(self, variables):
        try:
            self.queensRowsConflict(variables)
        except KeyError:
            return False
        return True

    def validDiagonals(self, variables):
        for idx, queen in enumerate(variables.queens[:-1]):
            for index, otherQueen in enumerate(variables.queens[(idx + 1):]):
                if queen.unassigned() or otherQueen.unassigned():
                    continue
                if abs(queen.value - otherQueen.value) == abs(idx - (index + 1 + idx)):
                    return False
        return True

    # def wipeout(self, variables, queen):
    #     removed = []
    #     for idx, queen in enumerate(variables.queens):
    #         if queen.value == -1:
    #             remove = set()
    #             for value in queen.domain:
    #                 queen.value = value
    #                 if not self.verify(variables):
    #                     remove.add(value)
    #                     removed.append((idx, value))
    #             queen.domain = queen.domain.difference(remove)
    #             queen.value = -1
    #     return removed

    def wipeout(self, variables, queen):
        queenNumber = variables.queens.index(queen) + 1
        queenToCheck = -1
        removed = []
        for constraint in self.set:
            if constraint[0] == queenNumber or constraint[1] == queenNumber:
                if constraint[0] == queenNumber and variables.queens[constraint[1] - 1].value == -1:
                    queenToCheck = variables.queens[constraint[1] - 1]
                if constraint[1] == queenNumber and variables.queens[constraint[0] - 1].value == -1:
                    queenToCheck = variables.queens[constraint[0] - 1]
                if queenToCheck == -1:
                    continue
                remove = set()
                for value in queenToCheck.domain:
                    queenToCheck.value = value 
                    if self.constraintFails(variables, constraint):
                        remove.add(value)
                        removed.append((variables.queens.index(queenToCheck), value))
                if len(queenToCheck.domain) == len(remove):
                    self.restore(variables, removed)
                    return None
                queenToCheck.domain = queenToCheck.domain.difference(remove)
                queenToCheck.value = -1
        return removed
    
    def verify(self, variables):
        for constraint in self.set:
            if self.constraintFails(variables, constraint):
                return False
        return True

    def constraintFails(self, variables, constraint):
        return constraint[2](variables, variables.queens[constraint[0] - 1], variables.queens[constraint[1] - 1])

    def restore(self, variables, domainTuples):
        for t in domainTuples:
            variables.queens[t[0]].domain.add(t[1])