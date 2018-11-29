import unittest
from variables import Variables


class Variable_Tests(unittest.TestCase):

    def test_variables_exist(self):
        variables = Variables()
        self.assertNotEqual(None, variables)

    def test_variables_has_eight_queens(self):
        variables = Variables()
        self.assertEqual(len(variables.queens), 8)

    def test_each_queen_has_a_domain(self):
        variables = Variables()
        self.assertNotEqual(None, variables.queens[0].domain)
        self.assertNotEqual(None, variables.queens[1].domain)
        self.assertNotEqual(None, variables.queens[2].domain)
        self.assertNotEqual(None, variables.queens[6].domain)
        self.assertNotEqual(None, variables.queens[7].domain)
