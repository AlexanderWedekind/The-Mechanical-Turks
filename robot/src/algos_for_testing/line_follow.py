from modules.state.robot.robot_parts import robotParts

def followLine():
    while True:
        robotParts['pirobot'].forwards(50)
