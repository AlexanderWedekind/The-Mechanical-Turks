from modules.state.robot.robot_parts import robotParts
import threading
from modules.state.robot.robot_state import robotState
import time

def readDistance():
    if robotState.watchingDistance == False:
        robotState.watchingDistance = True
        while robotState.watchingDistance == True:
            robotState.distance = round(robotParts.pirobot.ultrasonic.read(), 2)
            time.sleep(robotState.readDistanceTimeout)
        robotState.wasUsedWatchDistance = True

watchDistance = threading.Thread(target = readDistance)
