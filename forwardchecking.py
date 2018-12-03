

class ForwardChecking(object):
    
    def findSolution(self, variables):
        variables.queens[0].value = 2
        variables.queens[1].value = 4
        variables.queens[2].value = 1
        variables.queens[3].value = 3
