from modules.safe_call_with_except_logging import contCallLogExc
from modules.state.robot.robot_parts import robotParts
from modules.state.robot.road_markings import watchRoadMarkings
from modules.state.robot.robot_state import robotState
from modules.state.robot.get_distance import watchDistance

def pirobotCleanup():
    if watchDistance.is_alive():
        robotState.watchingDistance = False
        watchDistance.join()
    if watchRoadMarkings.is_alive():
        robotState.watchingRoadMarkings = False
        watchRoadMarkings.join()
    robotParts.pirobot.stop()
    print('- Pirobot cleaned up...')
    robotParts.pirobot = None

def motorsCleanup():
    robotParts.motors.stop()
    print('- Motors cleaned up...')
    robotParts.motors = None

def hardwareCleanup():
    if robotParts.pirobot != None:
        contCallLogExc(pirobotCleanup)
#    if robotParts['motors'] != None:
#        contCallLogExc(motorsCleanup)
        
 
