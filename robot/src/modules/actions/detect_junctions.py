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
    length = len(robotState['road_markings'])
    for i in range(robotState['junction_detect_time_interval'] * 10):
        if (length - i) > -1:
            if junctionDetected(robotState['road_markings'][length - i]) == True:
                return junctionDirection(robotState['road_markings'][length - i])
    return 'no'

