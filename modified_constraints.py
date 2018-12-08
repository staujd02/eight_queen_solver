from constraints import Constraints

class ModifiedConstraints(Constraints):

    def __init__(self, numberOfQueens):
        self.set = set()
        self.populateConstraints(self.set, numberOfQueens)

    def populateConstraints(self, mySet, numberOfQueens):
        self.rowConstraints(mySet, numberOfQueens)
        self.diagonalConstraints(mySet, numberOfQueens)

    def rowConstraints(self, set, numberOfQueens):
        for x in range(1, numberOfQueens):
            for y in range(x + 1, numberOfQueens + 1):
                set.add((x, y, lambda queen1, queen2: self.rowViolatesConstraint(
                    queen1, queen2)))

    def rowViolatesConstraint(self, queen1, queen2):
        return self.bothQueensHaveAValue(queen1, queen2) and queen1.value == queen2.value

    def diagonalConstraints(self, set, numberOfQueens):
        for x in range(1, numberOfQueens):
            for y in range(x + 1, numberOfQueens + 1):
                set.add(
                    (x, y, lambda queen1, queen2: self.diagonalViolatesConstraint(queen1, queen2)))

    def diagonalViolatesConstraint(self, queen1, queen2):
        return self.bothQueensHaveAValue(queen1, queen2) and (self.sameNegativeDiagonal(queen1, queen2) or self.samePositiveDiagonal(queen1, queen2))

    def sameNegativeDiagonal(self, queen1, queen2):
        return queen1.number + queen1.value == queen2.number + queen2.value
    
    def samePositiveDiagonal(self, queen1, queen2):
        return queen1.value - queen1.number == queen2.value - queen2.number

    def constraintFails(self, variables, constraint):
        return constraint[2](variables.queens[constraint[0] - 1], variables.queens[constraint[1] - 1])