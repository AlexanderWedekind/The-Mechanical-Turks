from pathlib import Path

def getPathToFile(segments):
    pathToSrc = Path('home/mechanical-turk/repos/The-Machanical-Turks/robot/src/')
    basePath = pathToSrc 
    unresolvedPathToRobot = pathToSrc / '..'
    pathToRobot = unresolvedPathToRobot.resolve()
    print(f"-- path to 'src':\n{pathToSrc}\n-- path to 'robot':\n{pathToRobot}")

    unresFilePath = basePath

    for segment in segments:
        unresFilePath = unresFilePath / segment
    
    print(f"-- resolved path tp file:\n{unresFilePath.resolve()}")
    return unresFilePath.resolve()

