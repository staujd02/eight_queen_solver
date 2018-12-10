
import unittest

from arc_consistentcy import ArcConsistency
from variables import Variables
from arcs import Arcs

class ArcConsistency_Tests(unittest.TestCase):

    def setUp(self):
        self.ac = ArcConsistency(Arcs(8))
    
    def test_arc_can_tell_when_a_solution_is_consistent(self):
        problem = Variables(8)
        self.assertTrue(self.ac.arcConsistent(problem))

    def test_arc_can_detect_an_inconsistency(self):
        problem = Variables(8)
        problem.queens[5].value = 5        
        problem.queens[1].value = 3        
        problem.queens[2].value = 1        
        problem.queens[3].value = 4        
        problem.queens[4].value = 7        
        self.assertFalse(self.ac.arcConsistent(problem))
    
    def test_constraints_can_detect_two_queens_in_the_same_diagonal(self):
        problem = Variables(8)
        problem.queens[0].value = 4
        problem.queens[3].value = 7
        self.assertFalse(self.ac.arcConsistent(problem))
    
    def test_constraints_can_detect_two_queens_in_the_opposing_diagonals(self):
        problem = Variables(8)
        problem.queens[4].value = 6
        problem.queens[7].value = 3
        self.assertFalse(self.ac.arcConsistent(problem))
    
    def test_constraints_can_detect_three_queens_in_the_same_diagonal(self):
        problem = Variables(8)
        problem.queens[0].value = 4
        problem.queens[2].value = 6
        problem.queens[3].value = 7
        self.assertFalse(self.ac.arcConsistent(problem))

    def test_constraints_can_detect_two_queens_in_the_same_rows(self):
        problem = Variables(8)
        problem.queens[0].value = 1
        problem.queens[7].value = 1
        self.assertFalse(self.ac.arcConsistent(problem))

    def test_constraints_can_detect_three_queens_in_the_same_rows(self):
        problem = Variables(8)
        problem.queens[0].value = 4
        problem.queens[1].value = 4
        problem.queens[2].value = 4
        self.assertFalse(self.ac.arcConsistent(problem))