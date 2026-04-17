from pathlib import Path

def getPathToFile(segments):
    filePath = Path('/home/mechanical-turk/repos/The-Mechanical-Turks/robot/src/')
    for segment in segments:
        filePath = filePath / segment
    
    print(f"-- resolved path to file:\n{filePath.resolve()}")
    return str(filePath.resolve())

