from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState

def drive(speed):
    robotState.currentSpeed = speed
    robotState.driving = True
    robotParts.pirobot.forward(robotState.currentSpeed)

def changeSpeed(speed):
    if robotState.driving == True:
        robotState.currentSpeed = speed
        robotParts.pirobot.forward(robotState.currentSpeed)
    else:
        robotState.currentSpeed = speed

class SetSpeed:
    def Go(self):
        drive(self.speed)
    def __init__(self, speed):
        self.speed = speed
        self.go = self.Go
    def __call__(self):
        changeSpeed(self.speed)

class SetDrivingSpeed:
    def Go(self):
        drive(robotState.currentSpeed)
    def Stop(self):
        robotState.driving = False
        robotParts.pirobot.forward(0)
    def __init__(self):
        self.go = self.Go
        self.stop = self.Stop
        self.forwards = SetSpeed(robotState.drivingSpeeds.forwards)
        self.reverse = SetSpeed(robotState.drivingSpeeds.reverse)
        self.forwardsLineFollow = SetSpeed(robotState.drivingSpeeds.forwardsLineFollow)
        self.reverseLineFollow = SetSpeed(robotState.drivingSpeeds.reverseLineFollow)
        self.cornering = SetSpeed(robotState.drivingSpeeds.cornering)
       
setDrivingSpeed = SetDrivingSpeed()

