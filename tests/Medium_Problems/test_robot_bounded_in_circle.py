import unittest
from Problems.Medium.robot_bounded_in_circle import is_robot_bounded


class TestRobotBoundedInCircle(unittest.TestCase):
    def test_is_robot_bounded_pass(self):
        instructions = "GGLLGG"
        self.assertTrue(is_robot_bounded(instructions))


if __name__ == '__main__':
    unittest.main()