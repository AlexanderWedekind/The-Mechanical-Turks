from modules.state.robot.robot_parts import robotParts
import threading
from modules.state.robot.robot_state import robotState
import time

def printRoadMarkings(changed = ""):
    print(f"-- Road Markings{changed}: [{robotState.roadMarkings[len(robotState.roadMarkings) - 1][0]}] [{robotState.roadMarkings[len(robotState.roadMarkings) - 1][1]}] [{robotState.roadMarkings[len(robotState.roadMarkings) - 1][2]}]")

def readRoadMarkings():
    if robotState.watchingRoadMarkings == False:
        robotState.watchingRoadMarkings = True
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
                for j in range(4):
                    if keptLineReads[j][i] != keptLineReads[j + 1][i]:
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
                if grayScaleReads[i] < (robotState.grayscaleSensitivity + (robotState.grayscaleSensitivity * robotState.grayscaleThresholdMargin)):
                    lineRead[i] = True
            return lineRead

        def addRoadMarkingsState():
            nonlocal keptLineReads
            stateChanged = False
            if consistentLineReads() == True:
                for i in range(3):
                    if keptLineReads[0][i] != robotState.road_markings[len(robotState.roadMarkings) - 1][i]:
                        stateChanged = True
            if stateChanged == True:
                robotState.road_markings.append(keptLineReads[0])
                robotState.changedRoadMarkings = True
            if len(robotState.roadMarkings) > 50:
                robotState.roadMarkings.pop(0)

        while robotState.watchingRoadMarkings == True:
            addLineRead(lineRead(robotParts.pirobot.get_grayscale_data()))
            addRoadMarkingsState()
            if robotState.changedRoadMarkings == True:
                printRoadMarkings(' changed')
                robotState.changedRoadMarkings = False
            time.sleep(robotState.readRoadMarkingsTimeout)
        robotState.wasUsedWatchRoadMarkings = True

watchRoadMarkings = threading.Thread(target = readRoadMarkings)

