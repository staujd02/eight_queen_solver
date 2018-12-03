import unittest

from forwardchecking import ForwardChecking
from variables import Variables

class ForwardChecking_Tests(unittest.TestCase):

    def setUp(self):
        self.forwardchecking = ForwardChecking()

    def test_forward_checking_exists(self):
        self.assertIsNotNone(self.forwardchecking)
    
    def test_backtracking_can_find_a_solution(self):
        problem = Variables(4)
        self.forwardchecking.findSolution(problem)
        self.assertTrue(self.fourByFourSolution(problem.queens) or self.altFourByFourSolution(problem.queens))

    def fourByFourSolution(self, queens):
        return queens[0].value == 3 and queens[1].value == 1 and queens[2].value == 4 and queens[3].value == 2   
    
    def altFourByFourSolution(self, queens):
        return queens[0].value == 2 and queens[1].value == 4 and queens[2].value == 1 and queens[3].value == 3   