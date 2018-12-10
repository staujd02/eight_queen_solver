import unittest

from variables import Variables
from arcs import Arcs
from global_arc_consistency import GlobalArcConsistency

class GAC_Tests(unittest.TestCase):

    def setUp(self):
        self.gac = GlobalArcConsistency(Arcs(8))

    def test_global_arc_consistency_can_find_a_solution(self):
        problem = Variables(4)
        gac = GlobalArcConsistency(Arcs(4))
        gac.findSolution(problem)
        self.assertTrue(self.fourByFourSolution(problem.queens) or self.altFourByFourSolution(problem.queens))
    
    def fourByFourSolution(self, queens):
        return queens[0].value == 3 and queens[1].value == 1 and queens[2].value == 4 and queens[3].value == 2   
    
    def altFourByFourSolution(self, queens):
        return queens[0].value == 2 and queens[1].value == 4 and queens[2].value == 1 and queens[3].value == 3   

    def test_global_arc_consistency_can_find_a_larger_solution(self):
        problem = Variables(8)
        gac = GlobalArcConsistency(Arcs(8))
        gac.findSolution(problem)
        for queen in problem.queens:
            self.assertNotEqual(-1, queen.value)