from modules.hardware_startup import robotParts
import threading
from modules.state.robot.robot_state import robotState
import time

def printRoadMarkings(changed = ""):
    print(f"-- Road Markings{changed}: [{robotState['road_markings']['left_sensor']}] [{robotState['road_markings']['middle_sensor']}] [{robotState['road_markings']['right_sensor']}]")

def readRoadMarkings():
    if robotState['watching_road_markings'] == False:
        robotState['watching_road_markings'] = True
        while robotState['watching_road_markings'] == True:
            grayScaleReadResult = robotParts['pirobot'].get_grayscale_data()
        #    print(f"-- grayScaleReadResult:\n{grayScaleReadResult}")
        #    roadMarkingsList = robotParts['pirobot'].get_line_status(grayScaleReadResult)
        #    print(f"-- roadMarkingsList:\n{roadMarkingsList}")
            if grayScaleReadResult[0] < robotState['grayscale_sensitivity']:
                if robotState['road_markings']['left_sensor'] == False:
                    robotState['road_markings']['left_sensor'] = True
                    robotState['changed_road_markings'] = True
            elif grayScaleReadResult[0] > robotState['grayscale_sensitivity']:
                if robotState['road_markings']['left_sensor'] == True:
                    robotState['road_markings']['left_sensor'] = False
                    robotState['changed_road_markings'] = True
            if grayScaleReadResult[1] < robotState['grayscale_sensitivity']:
                if robotState['road_markings']['middle_sensor'] == False:
                    robotState['road_markings']['middle_sensor'] = True
                    robotState['changed_road_markings'] = True
            elif grayScaleReadResult[1] > robotState['grayscale_sensitivity']:
                if robotState['road_markings']['middle_sensor'] == True:
                    robotState['road_markings']['middle_sensor'] = False
                    robotState['changed_road_markings'] = True
            if grayScaleReadResult[2] < robotState['grayscale_sensitivity']:
                if robotState['road_markings']['right_sensor'] == False:
                    robotState['road_markings']['right_sensor'] = True
                    robotState['changed_road_markings'] = True
            elif grayScaleReadResult[2] > robotState['grayscale_sensitivity']:
                if robotState['road_markings']['right_sensor'] == True:
                    robotState['road_markings']['right_sensor'] = False
                    robotState['changed_road_markings'] = True
            if robotState['changed_road_markings'] == True:
                printRoadMarkings(' changed')
                robotState['changed_road_markings'] = False
            time.sleep(0.01)
        robotState['was_used_watch_road_markings'] = True

def detectLine():
    readRoadMarkings()
    printRoadMarkings()

watchRoadMarkings = threading.Thread(target = readRoadMarkings)

