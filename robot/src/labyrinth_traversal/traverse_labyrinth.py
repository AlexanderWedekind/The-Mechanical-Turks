from modules.actions.line_navigation import lineFollowingThread
from modules.state.robot.robot_state import robotState

def TraverseLabyrinth():
    print("press SPACE to start line following. Q to exit")
    keyPress = input().lower()
    while keyPress != 'q':
        keyPress = input()
        if keyPress == ' ':
            lineFollow = lineFollowingThread()
            lineFollow.start()
    robotState['following_line'] = False
    lineFollow.join()




