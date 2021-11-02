import unittest
from unittest.result import TestResult
import super_algos

class TestFunctions(unittest.TestCase):
    def test_valid_list_min(self):
        """
        As a note this is done recursively and
        so only checks the current and next element
        """
        self.assertFalse(super_algos.valid_list_min([]))
        self.assertFalse(super_algos.valid_list_min(["a"]))
        self.assertFalse(super_algos.valid_list_min(["b",3]))
        self.assertFalse(super_algos.valid_list_min([2,"c"]))
        self.assertTrue(super_algos.valid_list_min([1,2]))
        self.assertTrue(super_algos.valid_list_min([3]))

    def test_find_min(self):
        self.assertTrue(super_algos.find_min([]) == -1)
        self.assertTrue(super_algos.find_min(["a",2,3]) == -1)
        self.assertTrue(super_algos.find_min([1,"b",3]) == -1)
        self.assertTrue(super_algos.find_min([1,2,"c"]) == -1)
        self.assertTrue(super_algos.find_min([1,2,3]) == 1)

    def test_valid_list_sum(self):
        """
        As a note this is done all at once
        """
        self.assertFalse(super_algos.valid_list_sum_all([], first = True))
        self.assertTrue(super_algos.valid_list_sum_all([], first = False))
        self.assertFalse(super_algos.valid_list_sum_all(["a"], first = False))
        self.assertFalse(super_algos.valid_list_sum_all(["b",3], first = False))
        self.assertFalse(super_algos.valid_list_sum_all([2,"c"], first = False))
        self.assertTrue(super_algos.valid_list_sum_all([1,2], first = False))
        self.assertTrue(super_algos.valid_list_sum_all([3], first = False))

    def test_sum_all(self):
        self.assertTrue(super_algos.sum_all([]) == -1)
        self.assertTrue(super_algos.sum_all(["a",2,3]) == -1)
        self.assertTrue(super_algos.sum_all([1,"b",3]) == -1)
        self.assertTrue(super_algos.sum_all([1,2,"c"]) == -1)
        self.assertTrue(super_algos.sum_all([1,2,3]) == 6)


    def test_valid_character_set(self):
        self.assertTrue(
            super_algos.valid_character_set(["a", "b"]))
        self.assertTrue(
            super_algos.valid_character_set(set(["a", "b"])))
        self.assertTrue(
            super_algos.valid_character_set(tuple(["a", "b"])))
        self.assertFalse(
            super_algos.valid_character_set([]))
        self.assertFalse(
            super_algos.valid_character_set([1, "b"]))
        self.assertFalse(
            super_algos.valid_character_set(set(["a", 2])))
        self.assertFalse(
            super_algos.valid_character_set(tuple([3, True])))

    def test_find_possible_strings(self):
        self.assertTrue(
            set(super_algos.find_possible_strings({"a","b"}, 2))\
            == {"aa","bb","ba","ab"})
        self.assertTrue(
            set(super_algos.find_possible_strings(["a","b"], 2))\
            == {"aa","bb","ba","ab"})
        self.assertTrue(
            super_algos.find_possible_strings([], 2) == [])
        self.assertTrue(
            set(super_algos.find_possible_strings(["a","b"], 0))\
            == {""})
        self.assertTrue(
            super_algos.find_possible_strings({1,"b"}, 2) == [])