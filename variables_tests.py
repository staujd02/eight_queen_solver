import unittest
from variables import Variables

class Variable_Tests(unittest.TestCase):

    def setUp(self):
        self.variables = Variables()

    def test_variables_has_eight_queens(self):
        self.assertEqual(len(self.variables.queens), 8)

    def test_each_queen_has_a_domain(self):
        self.assertNotEqual(None, self.variables.queens[0].domain)
        self.assertNotEqual(None, self.variables.queens[1].domain)
        self.assertNotEqual(None, self.variables.queens[2].domain)
        self.assertNotEqual(None, self.variables.queens[6].domain)
        self.assertNotEqual(None, self.variables.queens[7].domain)
    
    def test_a_queens_domain_is_a_set(self):
        self.assertEqual(type(set()), type(self.variables.queens[0].domain))