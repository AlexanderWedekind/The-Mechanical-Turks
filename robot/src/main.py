from modules.menus.main_menu import MainMenu
from hardware_initialisation import initHardware, hardwareCleanup
from safe_call_with_except_logging import crashCallLogExc, contCallLogExc

def Main():
    crashCallLogExc(initHardware)
    MainMenu()
    contCallLogExc(hardwareCleanup)

crashCallLogExc(Main)
