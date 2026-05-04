from modules.state.robot.robot_parts import robotParts
import threading
from modules.state.robot.robot_state import robotState
import time

def printRoadMarkings(changed = ""):
    print(f"-- Road Markings{changed}: [{robotState['road_markings'][0]}] [{robotState['road_markings'][1]}] [{robotState['road_markings'][2]}]")

def readRoadMarkings():
    if robotState['watching_road_markings'] == False:
        robotState['watching_road_markings'] = True
        keptLineReads = [
                [False, False, False],
                [False, False, False],
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ]

        def consistentLineReads():
            nonlocal keptLineReads
            consistent = True
            for i in range(3):
                if consistent == False:
                    break
                else:
                    for j in range(4):
                        if keptLineReads[j][i] == keptLineReads[j + 1][i]:
                            consistent = True
                        else:
                            consistent = False
                            break
            return consistent

        def addLineRead(reads):
            nonlocal keptLineReads
            keptLineReads.pop(0)
            keptLineReads.append(reads)

        def lineRead(grayScaleReads):
            lineRead = [False, False, False]
            for i in range(3):
                if grayScaleReads[i] < (robotState['grayscale_sensitivity'] + (robotState['grayscale_sensitivity'] * robotState['grayscale_threshold_margin'])):
                    lineRead[i] = True
            return lineRead

        def addRoadMarkingsState():
            nonlocal keptLineReads
            if consistentLineReads() == True:
                for i in range(3):
                    if keptLineReads[0][i] != robotState['road_markings'][i]:
                        robotState['road_markings'][i] = keptLineReads[0][i]
                        robotState['changed_road_markings'] = True

        while robotState['watching_road_markings'] == True:
            addLineRead(lineRead(robotParts['pirobot'].get_grayscale_data()))
            addRoadMarkingsState()
            if robotState['changed_road_markings'] == True:
                printRoadMarkings(' changed')
                robotState['changed_road_markings'] = False
            time.sleep(robotState['read_road_markings_timeout'])
        robotState['was_used_watch_road_markings'] = True

watchRoadMarkings = threading.Thread(target = readRoadMarkings)

