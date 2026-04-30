from modules.state.robot.robot_parts import robotParts

def lineFollow():
    while True:
        robotParts['pirobot'].forwards(50)
