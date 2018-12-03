import unittest

from backtracking import BackTracking
from variables import Variables

class BackTracking_Tests(unittest.TestCase):

    def setUp(self):
        self.variables = Variables(8)
        self.backtracking = BackTracking()

    def test_backtracking_can_find_a_solution(self):
        problem = Variables(4)
        self.backtracking.findSolution(problem)
        self.assertTrue(self.fourByFourSolution(problem.queens) or self.altFourByFourSolution(problem.queens))
    
    def test_backtracking_can_find_a_larger_solution(self):
        problem = Variables(8)
        problem.queens[4].value = 5
        self.backtracking.findSolution(problem)
        self.assertNotEqual(-1, problem.queens[0].value)
        self.assertNotEqual(-1, problem.queens[1].value)
        self.assertNotEqual(-1, problem.queens[2].value)
        self.assertNotEqual(-1, problem.queens[4].value)
        self.assertNotEqual(-1, problem.queens[6].value)
        self.assertNotEqual(-1, problem.queens[7].value)

    def fourByFourSolution(self, queens):
        return queens[0].value == 3 and queens[1].value == 1 and queens[2].value == 4 and queens[3].value == 2   
    
    def altFourByFourSolution(self, queens):
        return queens[0].value == 2 and queens[1].value == 4 and queens[2].value == 1 and queens[3].value == 3   