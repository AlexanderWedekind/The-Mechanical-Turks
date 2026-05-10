from modules.state.robot.robot_state import robotState

def junctionDirection(values):
    finding = ""
    if values[1] == True:
        if values[0] == True:
            finding = 'left'
        elif values[2] == True:
            finding = 'right'
        elif values[0] == True & values[2] == True:
            finding = 'crossroads'
        else:
            finding = 'no'
    else:
        finding = 'passed'
    return finding

def junctionDetected(values):
    finding = False
    if values[1] == True:
        if values[0] == True | values[2] == True:
            finding = True
    return finding

def findJunction():
    length = len(robotState.roadMarkings)
    for i in range(robotState.junctionDetectTimeInterval * 10):
        if (length - i) > -1:
            if junctionDetected(robotState.roadMarkings[length - i]) == True:
                return junctionDirection(robotState.roadMarkings[length - i])
    return 'no'

