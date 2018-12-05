
class Variables(object):

    def __init__(self, domainRange):
        self.queens = []
        i = 0
        while i < domainRange:
            i += 1
            self.queens.append(Queen(domainRange, i)) 

    def copy(self):
        new = Variables(len(self.queens))
        for idx, queen in enumerate(self.queens):
            new.queens[idx].value = queen.value
            new.queens[idx].domain = set(queen.domain)
        return new

class Queen(object):

    def __init__(self, domainRange, columnNumber):
       self.domain = set(range(1, domainRange + 1))
       self.value = -1
       self.number = columnNumber
    
    def __str__(self):
     return "{Value: " + str(self.value) + "| Domain: [" + str(self.domain) + "]}"

    def unassigned(self):
        return self.value == -1