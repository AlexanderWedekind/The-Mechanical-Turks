from modules.hardware_startup import robotParts
import threading
from modules.state.robot.robot_state import robotState

roadMarkings = {
        'leftSensor': False,
        'middleSensor': False,
        'rightSensor': False
        }

def printRoadMarkings():
    print(f"-- Road Markings --\n[{roadMarkings['leftSensor']}] [{roadMarkings['middleSensor']}] [{roadMarkings['rightSensor']}]")
def readRoadMarkings():
    if robotState['watching_road_markings'] == False:
        robotState['watching_road_markings'] = True
        while robotState['watching_road_markings'] == True:
            grayScaleReadResult = robotParts['pirobot'].get_grayscale_data()
        #    print(f"-- grayScaleReadResult:\n{grayScaleReadResult}")
        #    roadMarkingsList = robotParts['pirobot'].get_line_status(grayScaleReadResult)
        #    print(f"-- roadMarkingsList:\n{roadMarkingsList}")
            if grayScaleReadResult[0] < 400:
                roadMarkings['leftSensor'] = True
            else:
                roadMarkings['leftSensor'] = False
            if grayScaleReadResult[1] < 400:
                roadMarkings['middleSensor'] = True
            else:
                roadMarkings['middleSensor'] = False
            if grayScaleReadResult[2] < 400:
                roadMarkings['rightSensor'] = True
            else:
                roadMarkings['rightSensor'] = False
        robotState['was_used_watch_road_markings'] = True

def detectLine():
    readRoadMarkings()
    printRoadMarkings()

watchRoadMarkings = threading.Thread(target = readRoadMarkings)

