from picarx import Picarx
from robot_hat import Music
from robot_hat import TTS
from robot_hat import Motors
from modules.safe_call_with_except_logging import contCallLogExc
from modules.hardware_startup import robotParts

def pirobotCleanup():
    robotParts['pirobot'].stop()
    print('- Pirobot cleaned up...')
    robotParts['pirobot'] = None

def hardwareCleanup():
    if robotParts['pirobot'] != None:
        if robotParts['pirobot'] != None:
            contCallLogExc(pirobotCleanup)
 
