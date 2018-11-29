
class Variables(object):

    def __init__(self):
        self.queens = []
        i = 0
        while i < 8:
            i += 1
            self.queens.append(Queen()) 

class Queen(object):

    def __init__(self):
       self.domain = set([1,2,3,4,5,6,7,8])