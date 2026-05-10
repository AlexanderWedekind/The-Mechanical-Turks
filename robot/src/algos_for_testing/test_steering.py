from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState

def testSteering():
    print("-- press L to test steering left (L: hard left; l: shallow left); R and r for right; press Q to quit")
    keyPress = ""
    while keyPress != 'q':
        keyPress = input()
        match keyPress:
            case 'L':

