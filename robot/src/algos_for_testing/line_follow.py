from modules.state.robot.road_markings import roadMarkings, readRoadMarkings
from modules.state.robot.robot_parts import robotParts

def followLine():
    while True:
        robotParts['pirobot'].forwards(50)
