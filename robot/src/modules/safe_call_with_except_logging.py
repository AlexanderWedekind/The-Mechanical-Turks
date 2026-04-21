import traceback
from modules.hardware_initialisation import hardwareCleanup

def contCallLogExc(function, *args):
    try:
        return function(*args)
    except Exception as e:
        print(f"-- Exception --\nType: {type(e)}\nMessage:\n{e}\nArgs: {e.args}\nTraceback:")
        traceback.print_exc()

def crashCallLogExc(function, *args):
    try:
        return function(*args)
    except Exception as e:
        print(f"-- Exception --\nType: {type(e)}\nMessage:\n{e}\nArgs: {e.args}\nTraceback:")
        traceback.print_exc()
    contCallLogExc(hardwareCleanup)
    raise

