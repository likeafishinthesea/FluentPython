import unittest
from Problems.Medium.average_waiting_time import calculate_average_waiting_time


class TestAverageWaitingTime(unittest.TestCase):
    def test_calculate_average_waiting_time_gap_arrival(self):
        customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
        expected_avg_time = 3.25
        actual_avg_time = calculate_average_waiting_time(customers=customers)
        self.assertEqual(first=expected_avg_time, second=actual_avg_time)

    def test_calculate_average_waiting_time_stack_arrival(self):
        customers = [[1, 2], [2, 5], [4, 3]]
        expected_avg_time = 5
        actual_avg_time = calculate_average_waiting_time(customers=customers)
        self.assertEqual(first=expected_avg_time, second=actual_avg_time)


if __name__ == '__main__':
    unittest.main()
