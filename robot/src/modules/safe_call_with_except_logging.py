import traceback

def getCleanupModule():
    from modules.hardware_cleanup import hardwareCleanup
    return hardwareCleanup

def contCallLogExc(function, *args):
    try:
        return function(*args)
    except Exception as e:
        print(f"-- Exception --\nType: {type(e)}\nMessage:\n{e}\nArgs: {e.args}\nTraceback:")
        traceback.print_exc()

def crashCallLogExc(function, *args):
    cleanup = getCleanupModule()
    try:
        return function(*args)
    except Exception as e:
        print(f"-- Exception --\nType: {type(e)}\nMessage:\n{e}\nArgs: {e.args}\nTraceback:")
        traceback.print_exc()
    contCallLogExc(cleanup)
    raise

