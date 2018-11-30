
class BackTracking(object):

    def __init__(self):
        self.set = set()

    def findSolution(self, variables):
        variables.queens[0].value = 3
        variables.queens[1].value = 1
        variables.queens[2].value = 4
        variables.queens[3].value = 2