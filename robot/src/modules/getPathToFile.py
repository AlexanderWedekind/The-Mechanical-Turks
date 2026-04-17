from pathlib import Path

def getPathToFile(segments):
    pathToSrc = Path('/home/mechanical-turk/repos/The-Machanical-Turks/robot/src/')
    print(f"-- pathToSrc:\n{pathToSrc}")
    print(f"-- resolved psthToSrc:\n{pathToSrc.resolve()}")
    basePath = pathToSrc 
    print(f"-- basePath:\n{basePath}")
    print(f"-- resolved basePath:\n{basePath.resolve()}")
    unresolvedPathToRobot = pathToSrc / '..'
    print(f"-- 'pathToSrc+/+..':\n{unresolvedPathToRobot}")
    print(f"-- resolved 'pathToSrc+/+..':\n{unresolvedPathToRobot.resolve()}")
    pathToRobot = unresolvedPathToRobot.resolve()
    print(f"-- path to 'robot':\n{unresolvedPathToRobot}\n-- resolved path to 'robot':\n{pathToRobot}")

    unresFilePath = basePath

    for segment in segments:
        unresFilePath = unresFilePath / segment
    
    print(f"-- resolved path to file:\n{unresFilePath.resolve()}")
    return unresFilePath.resolve()

