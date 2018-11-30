
class Variables(object):

    def __init__(self, number):
        self.queens = []
        i = 0
        while i < number:
            i += 1
            self.queens.append(Queen(number)) 

class Queen(object):

    def __init__(self, number):
       self.domain = set(range(1,number + 1))
       self.value = -1
    
    def __str__(self):
     return "{Value: " + str(self.value) + "| Domain: [" + str(self.domain) + "]}"

    def unassigned(self):
        return self.value == -1