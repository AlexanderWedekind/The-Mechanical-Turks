from modules.state.robot.road_markings import roadMarkings, readRoadMarkings
from modules.hardware_startup import robotParts

def followLine():
    while True:
        robotParts['pirobot'].forwards(50)
