import unittest
from Problems.Python.Easy import merge_alternately


class MergeStringsAlternately(unittest.TestCase):
    def test_merge_alternately_equal_str_len(self):
        word1 = "abc"
        word2 = "pqr"
        expected_merge = "apbqcr"
        actual_merge = merge_alternately(word1, word2)
        self.assertEqual(first=expected_merge, second=actual_merge)

    def test_merge_alternately_not_qual_str_len_1(self):
        word1 = "ab"
        word2 = "pqrs"
        expected_merge = "apbqrs"
        actual_merge = merge_alternately(word1, word2)
        self.assertEqual(first=expected_merge, second=actual_merge)

    def test_merge_alternately_not_qual_str_len_2(self):
        word1 = "abcd"
        word2 = "pq"
        expected_merge = "apbqcd"
        actual_merge = merge_alternately(word1, word2)
        self.assertEqual(first=expected_merge, second=actual_merge)


if __name__ == '__main__':
    unittest.main()