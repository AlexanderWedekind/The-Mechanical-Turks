from modules.state.robot.robot_parts import robotParts

def MeasureDistance():
    distance = robotParts['pirobot'].ultrasonic.read()
    print('-- distance measured: ' + str(distance))
    return distance


