from modules.hardware_startup import robotParts
from modules.state.road_markings import roadMarkings, printRoadMarkings

def readRoadMarkings():
    grayScaleReadResult = robotParts['pirobot'].get_grayscale_data()
    print(f"-- grayScaleReadResult:\n{grayScaleReadResult}")
    roadMarkingsList = robotParts['pirobot'].get_line_status(grayScaleReadResult)
    print(f"-- roadMarkingsList:\n{roadMarkingsList}")
    if roadMarkingsList[0] == 0:
        roadMarkings['leftSensor'] = True
    else:
        roadMarkings['leftSensor'] = False
    if roadMarkingsList[1] == 0:
        roadMarkings['middleSensor'] = True
    else:
        roadMarkings['middlesensor'] = False
    if roadMarkingsList[2] == 0:
        roadMarkings['rightSensor'] = True
    else:
        roadMarkings['rightSensor'] = False

def detectLine():
    readRoadMarkings()
    printRoadMarkings()
