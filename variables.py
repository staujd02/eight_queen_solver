
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
       self.value = -1
    
    
    def __str__(self):
     return "{Value: " + str(self.value) + "| Domain: [" + str(self.domain) + "]}"

    def unassigned(self):
        return self.value == -1