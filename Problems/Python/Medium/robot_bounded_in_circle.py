"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.

"""


def is_robot_bounded(instructions: str) -> bool:
    position = (0, 0)
    direction = "N"
    for inst in instructions:
        if inst == "L" and direction == "N":
            direction = "W"
        elif inst == "L" and direction == "W":
            direction = "S"
        elif inst == "L" and direction == "S":
            direction = "E"
        elif inst == "L" and direction == "E":
            direction = "N"
        elif inst == "R" and direction == "N":
            direction = "E"
        elif inst == "R" and direction == "E":
            direction = "S"
        elif inst == "R" and direction == "S":
            direction = "W"
        elif inst == "R" and direction == "W":
            direction = "N"

        if inst == "G" and direction == "N":
            position = (position[0], position[1] + 1)
        elif inst == "G" and direction == "E":
            position = (position[0] + 1, position[1])
        elif inst == "G" and direction == "W":
            position = (position[0] - 1, position[1])
        elif inst == "G" and direction == "S":
            position = (position[0], position[1] - 1)
    return True if position == (0, 0) or direction != "N" else False


example_instructions = "LLGRL"
print(is_robot_bounded(example_instructions))






