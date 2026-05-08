from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState
from modules.actions.drive import setDrivingSpeed

def testDriving():
    print("-- Press F to start driving; S to stop; Q to quit")
    keyPress = ""
    while keyPress != 'q':
        keyPress = input().lower()
        if keyPress == 'f':
            setDrivingSpeed.forwards()
        if keyPress == 's':
            setDrivingSpeed.stop()
            
 
