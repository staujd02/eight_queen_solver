
class Variables(object):

    def __init__(self):
        self.queens = []
        i = 0
        while i < 8:
            i += 1
            self.queens.append(Queen()) 

class Queen(object):

    def __init__(self):
       self.domain = set() 