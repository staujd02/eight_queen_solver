import unittest

from better_constraints import BetterConstraints
from variables import Variables

class Better_Constraints_Tests(unittest.TestCase):

    def setUp(self):
        self.constraints = BetterConstraints(8)
        self.variables = Variables(8)

    def test_constraints_is_composed_of_three_sets(self):
        constraints = BetterConstraints(4)
        self.assertTrue(constraints.rows.issuperset(set([1,2,4])))
        self.assertTrue(constraints.negativeDiagonals.issuperset(set([-3,-1,1,3])))
        self.assertTrue(constraints.positiveDiagonals.issuperset(set([2,3,6,8])))
        self.assertFalse(constraints.positiveDiagonals.issuperset(set([9, 1])))
        self.assertFalse(constraints.negativeDiagonals.issuperset(set([-4, 4])))
    
    def test_constraints_is_composed_of_three_sets_that_expand_with_number_of_queens(self):
        self.assertTrue(self.constraints.rows.issuperset(set([1,2,4,8])))
        self.assertTrue(self.constraints.negativeDiagonals.issuperset(set([-7,-3,-1,1,3,7])))
        self.assertTrue(self.constraints.positiveDiagonals.issuperset(set([2,3,6,8,16])))
        self.assertFalse(self.constraints.positiveDiagonals.issuperset(set([17, 1])))
        self.assertFalse(self.constraints.negativeDiagonals.issuperset(set([-8, 8])))

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


    def test_contraints_will_prune_domains(self):
        self.variables.queens[0].value = 1
        self.variables.queens[1].value = 3
        self.constraints.wipeout(self.variables)
        self.assertEqual(set([2, 4, 5, 6, 7, 8]), self.constraints.rows)
        self.assertEqual(set([3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), self.constraints.positiveDiagonals)
        self.assertEqual(set([-7, -6, -5, -4, -3, -2, -1, 2, 3, 4, 5, 6, 7]), self.constraints.negativeDiagonals)

    # def test_contraints_will_prune_domains(self):
    #     self.variables.queens[0].value = 1
    #     self.constraints.wipeout(self.variables, self.variables.queens[0])
    #     self.variables.queens[1].value = 3
    #     self.constraints.wipeout(self.variables, self.variables.queens[1])
    #     self.assertEqual(set([5, 6, 7, 8]), self.variables.queens[2].domain)
    #     self.assertEqual(set([2, 6, 7, 8]), self.variables.queens[3].domain)
    #     self.assertEqual(set([2, 4, 7, 8]), self.variables.queens[4].domain)
    #     self.assertEqual(set([2, 4, 5, 6, 7]), self.variables.queens[7].domain)
    
    def test_contraints_will_return_nothing_when_assigned_values_wipeout_a_domain(self):
        self.variables.queens[0].value = 2
        self.variables.queens[1].value = 4
        self.variables.queens[2].value = 1
        self.variables.queens[3].value = 3
        self.variables.queens[4].value = 5
        self.assertEqual(None, self.constraints.wipeout(self.variables))

    # def test_constraints_will_return_the_pruned_values(self):
    #     self.variables.queens[0].value = 1
    #     values = self.constraints.wipeout(self.variables, self.variables.queens[0])
    #     self.assertItemsEqual([(3, 1), (2, 3), (7, 8), (2, 1), (7, 1), (5, 6), (4, 1), (4, 5), (5, 1), (1, 2), (3, 4), (6, 1), (1, 1), (6, 7)], values)
    
    # def test_constraints_can_restore_domains(self):
    #     self.variables.queens[0].value = 1
    #     values = self.constraints.wipeout(self.variables, self.variables.queens[0])
    #     self.constraints.restore(self.variables, values)
    #     self.assertEqual(set([1,2,3,4,5,6,7,8]), self.variables.queens[0].domain)
    #     self.assertEqual(set([1,2,3,4,5,6,7,8]), self.variables.queens[1].domain)
    #     self.assertEqual(set([1,2,3,4,5,6,7,8]), self.variables.queens[7].domain)
