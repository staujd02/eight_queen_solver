
class Constraints(object):

    def __init__(self):
        self.set = set()

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

    def wipeout(self, variables, queen):
        removed = []
        for idx, queen in enumerate(variables.queens):
            if queen.value == -1:
                remove = set()
                for value in queen.domain:
                    queen.value = value
                    if not self.verify(variables):
                        remove.add(value)
                        removed.append((idx, value))
                queen.domain = queen.domain.difference(remove)
                queen.value = -1
        return removed
    
    def verify(self, variables):
        if self.validRows(variables):
            return self.validDiagonals(variables)
        return False

    def restore(self, variables, domainTuples):
        for t in domainTuples:
            variables.queens[t[0]].domain.add(t[1])