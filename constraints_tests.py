import unittest

from constraints import Constraints
from variables import Variables

class Variable_Tests(unittest.TestCase):

    def setUp(self):
        self.constraints = Constraints()
        self.variables = Variables(8)

    def test_constraints_exist(self):
        self.assertNotEqual(None, self.constraints)
    
    def test_constraints_can_detect_two_queens_in_the_same_diagonal(self):
        self.variables.queens[0].value = 4
        self.variables.queens[3].value = 7
        self.assertEqual(False, self.constraints.verify(self.variables))
    
    def test_constraints_can_detect_two_queens_in_the_opposing_diagonals(self):
        self.variables.queens[4].value = 6
        self.variables.queens[7].value = 3
        self.assertEqual(False, self.constraints.verify(self.variables))
    
    def test_constraints_can_detect_three_queens_in_the_same_diagonal(self):
        self.variables.queens[0].value = 4
        self.variables.queens[2].value = 6
        self.variables.queens[3].value = 7
        self.assertEqual(False, self.constraints.verify(self.variables))

    def test_constraints_can_detect_two_queens_in_the_same_rows(self):
        self.variables.queens[0].value = 1
        self.variables.queens[7].value = 1
        self.assertEqual(False, self.constraints.verify(self.variables))

    def test_constraints_can_detect_three_queens_in_the_same_rows(self):
        self.variables.queens[0].value = 4
        self.variables.queens[1].value = 4
        self.variables.queens[2].value = 4
        self.assertEqual(False, self.constraints.verify(self.variables))

    def test_constraints_will_allow_unassigned_values_to_pass_constraints(self):
        self.variables.queens[0].value = 1
        self.variables.queens[1].value = 3
        self.assertEqual(True, self.constraints.verify(self.variables))