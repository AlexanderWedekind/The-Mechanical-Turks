from modules.hardware_startup import robotParts
import threading
from modules.state.robot.robot_state import robotState

def readDistance():
    if robotState['watching_distance'] == False:
        robotState['watching_distance'] = True
        while robotState['watching_distance'] == True:
            robotState['distance'] = robotParts['pirobot'].get_distance_reading()
        robotState['was_used_watch_distance'] = True

watchDistance = threading.Thread(target = readDistance)
