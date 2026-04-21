from modules.menus.main_menu import MainMenu
from modules.hardware_startup import initHardware
from modules.hardware_cleanup import hardwareCleanup
from modules.safe_call_with_except_logging import crashCallLogExc, contCallLogExc

def Main():
    crashCallLogExc(initHardware)
    MainMenu()
    contCallLogExc(hardwareCleanup)

crashCallLogExc(Main)
