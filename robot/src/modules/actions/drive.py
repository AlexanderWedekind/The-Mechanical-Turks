from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState

class SetDrivingSpeed:
    def drive(self, speed):
        robotState['current_speed'] = speed
        robotState['driving'] = True
        robotParts['pirobot'].forward(speed)
    def forwards(self):
        self.drive(robotState['driving_speeds']['forwards'])
    def stop(self):
        robotState['driving'] = False
        robotState['current_speed'] = robotState['driving_speeds']['stopped']
        robotParts['pirobot'].forward(robotState['current_speed'])
    def reverse(self):
        self.drive(robotState['driving_speeds']['reverse'])
    def forwardsLineFollow(self):
        self.drive(robotState['driving_speeds']['forwards_line_follow'])
    def reverseLineFollow(self):
        self.drive(robotState['driving_speeds']['reverse_line_follow'])
    def cornering(self):
        self.drive(robotState['driving_speeds']['cornering'])
        
setDrivingSpeed = SetDrivingSpeed()

