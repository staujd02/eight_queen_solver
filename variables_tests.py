import unittest
from variables import Variables

class Variable_Tests(unittest.TestCase):

    def setUp(self):
        self.variables = Variables(8)

    def test_variables_has_a_number_of_queens(self):
        varis = Variables(6)
        self.assertEqual(6, len(varis.queens))

    def test_each_queen_has_a_domain(self):
        self.assertNotEqual(None, self.variables.queens[0].domain)
        self.assertNotEqual(None, self.variables.queens[1].domain)
        self.assertNotEqual(None, self.variables.queens[2].domain)
        self.assertNotEqual(None, self.variables.queens[6].domain)
        self.assertNotEqual(None, self.variables.queens[7].domain)

    def test_a_queens_domain_is_a_set_containg_a_range_from_1_to_8(self):
        self.assertEqual(self.variables.queens[0].domain.issubset([1,2,3,4,5,6,7,8]), True)
    
    def test_a_queen_has_a_value_initialized_to_negative_one(self):
        self.assertEqual(self.variables.queens[0].value, -1)
    
    def test_a_copy_variable_list_is_indepentent(self):
        varis = Variables(4)
        newVaris = varis.copy()
        varis.queens[0].value = 1
        varis.queens[0].domain = set([1, 2, 3])
        self.assertNotEqual(1, newVaris.queens[0].value)
        self.assertNotEqual(set([1, 2, 3]), newVaris.queens[0].domain)
