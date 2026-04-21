from modules.hardware_startup import robotParts

def MeasureDistance():
    distance = robotParts['pirobot'].ultrasonic.read()
    print('-- distance measured: ' + str(distance))
    return distance


