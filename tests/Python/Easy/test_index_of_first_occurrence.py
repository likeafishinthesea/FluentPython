import unittest
from Problems.Python.Easy.Index_of_first_occurrence import get_index_of_first_occur


class TestSolution(unittest.TestCase):
    def test_merge_alternately_equal_str_len(self):
        needle = "ll"
        haystack = "hello"
        expected_output = 2
        actual_merge = get_index_of_first_occur(haystack, needle)
        self.assertTrue(expected_output == actual_merge)


if __name__ == '__main__':
    unittest.main()