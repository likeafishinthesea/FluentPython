import unittest
import pandas as pd

from pandas.testing import assert_frame_equal

from Problems.Database.Medium.second_highest_salary import get_second_highest_salary


class TestSecondHighestSalary(unittest.TestCase):

    def setUp(self) -> None:
        self.df_one_salary = pd.DataFrame(columns=["id", "salary"], data=[[1, 100]])
        self.df_two_equal_salary = pd.DataFrame(columns=["id", "salary"], data=[[1, 100], [2, 100]])
        self.df_more_than_one_salary = pd.DataFrame(columns=["id", "salary"], data=[[1, 100], [2, 200], [3, 200], [4, 300]])
        self.df_expected_none = pd.DataFrame(columns=["SecondHighestSalary"], data=[None])
        self.df_expected_highest_second_salary = pd.DataFrame(columns=["SecondHighestSalary"], data=[200])

    def test_second_highest_salary_return_none(self):
        assert_frame_equal(get_second_highest_salary(employee=self.df_one_salary), self.df_expected_none)

    def test_second_highest_salary_return_none_2(self):
        assert_frame_equal(get_second_highest_salary(employee=self.df_two_equal_salary), self.df_expected_none)

    def test_second_highest_salary_return_second_highest_salary(self):
        assert_frame_equal(get_second_highest_salary(employee=self.df_more_than_one_salary), self.df_expected_highest_second_salary)


if __name__ == '__main__':
    unittest.main()

