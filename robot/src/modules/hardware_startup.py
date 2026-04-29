import threading
from picarx import Picarx
from robot_hat import Music
from robot_hat import TTS
from robot_hat import Motors
from modules.safe_call_with_except_logging import crashCallLogExc
from modules.state.robot.robot_state import robotState
from modules.state.robot.road_markings import watchRoadMarkings
from modules.state.robot.get_distance import watchDistance

robotParts = {
        'pirobot' : None,
        'music': None,
        'tts': None,
        'motors': None
        }

def initPirobot():
    robotParts['pirobot'] = Picarx()
    print('- Pirobot initialised...')

def initMusic():
    robotParts['music'] = Music()
    print('- Music initialised...')

def initTTS():
    robotParts['tts'] = TTS()
    print('- TTS initialised...')

def initMotors():
    robotParts['motors'] = Motors()
    print('- Motors initialised...')

def startWatchingRoadMarkings():
    if robotState['was_used_watch_road_markings'] == False:
        if watchRoadMarkings.is_alive() == False:
            watchRoadMarkings.start()
        else:
            print("--> road marking thread allready alive -> no started again")
    print("--> road marking thread cannot be used twice")

def startWatchingDistance():
    if robotState['was_used_watch_distance'] == False:
        if watchDistance.is_alive() == False:
            watchDistance.start()
        else:
            print("--> watch distance thread allready alive -> not started again")
    print("--> watch distance thread can only be used once")

def initHardware():
    if robotParts['pirobot'] == None:
        crashCallLogExc(initPirobot)
    if robotParts['music'] == None:
        crashCallLogExc(initMusic)
    if robotParts['tts'] == None:
        crashCallLogExc(initTTS)
#    if robotParts['motors'] == None:
#        crashCallLogExc(initMotors)
    crashCallLogExc(startWatchingRoadMarkings)
    crashCallLogExc(startWatchingDistance)

