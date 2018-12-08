
import unittest

from arc_consistentcy import ArcConsistency
from variables import Variables
from constraints import Constraints

class ArcConsistency_Tests(unittest.TestCase):

    def setUp(self):
        self.forwardchecking = ArcConsistency(Constraints(8))

    def test_backtracking_can_find_a_solution(self):
        problem = Variables(4)
        ac = ArcConsistency(Constraints(4))
        ac.findSolution(problem)
        self.assertTrue(self.fourByFourSolution(problem.queens) or self.altFourByFourSolution(problem.queens))
    
    # def test_backtracking_can_find_a_larger_solution(self):
    #     problem = Variables(8)
    #     forwardchecking = ArcConsistency(Constraints(8))
    #     forwardchecking.findSolution(problem)
    #     for queen in problem.queens:
    #         self.assertNotEqual(-1, queen.value)

    def fourByFourSolution(self, queens):
        return queens[0].value == 3 and queens[1].value == 1 and queens[2].value == 4 and queens[3].value == 2   
    
    def altFourByFourSolution(self, queens):
        return queens[0].value == 2 and queens[1].value == 4 and queens[2].value == 1 and queens[3].value == 3   