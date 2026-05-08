from modules.actions.line_navigation import lineFollowingThread
from modules.state.robot.robot_state import robotState
from modules.state.environment.labyrinth import 

def TraverseLabyrinth():
    print("press F to start line following. Q to exit")
    keyPress = input().lower()
    while keyPress != 'q':
        keyPress = input()
        if keyPress == 'f':
            lineFollow = lineFollowingThread()
            lineFollow.start()
    if lineFollow.is_alive():
        robotState['following_line'] = False
        lineFollow.join()




