from picarx import Picarx
from robot_hat import Music
from robot_hat import TTS
from robot_hat import Motors
from modules.safe_call_with_except_logging import crashCallLogExc

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

def initHardware():
    if robotParts['pirobot'] == None:
        crashCallLogExc(initPirobot)
    if robotParts['music'] == None:
        crashCallLogExc(initMusic)
    if robotParts['tts'] == None:
        crashCallLogExc(initTTS)
    if robotParts['motors'] == None:
        crashCallLogExc(initMotors)

