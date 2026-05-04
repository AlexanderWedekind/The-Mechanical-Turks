from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState
from modules.actions.drive import DrivingSpeed
drivingSpeed = DrivingSpeed()

def testDriving():
    print("-- Press F to start driving; S to stop; Q to quit")
    keyPress = input().lower()
    while keyPress != 'q':
        keyPress = input().lower()
        if keyPress == 'f':
            drivingSpeed.forwards()
        if keyPress == 's':
            drivingSpeed.stop()
            
 
