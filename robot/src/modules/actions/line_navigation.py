from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState
import threading

def followLine():
    if robotState['following_line'] == False:
        robotState['following_line'] = True
        while robotState['following_line'] == True:
            if robotState['driving'] == False:
                if robotState['current_speed'] != robotState['driving_speeds']['forwards_line_follow']:
                    robotState['current_speed'] = robotState['driving_speeds']['forwards_line_follow']
                robotParts['pirobot'].forward(robotState['current_speed'])
                robotState['driving'] = True
            else:
                if robotState['current_speed'] != robotState['driving_speeds']['forwards_line_follow']:
                    robotState['current_speed'] = robotState['driving_speeds']['forwards_line_follow']
                robotParts['pirobot'].forward(robotState['current_speed'])
            if robotState['road_markings']['middle_sensor'] == True:
                robotState['current_steering_angle'] = robotState['current_steering_angle'] * -1
                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])
            if robotState['road_markings']['left_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
                robotState['current_steering_angle'] = robotState['steering_angles']['shallow_right']
                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])
            if robotState['road_markings']['right_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
                robotState['current_steering_angle'] = robotState['steering_angles']['shallow_left']
                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])

def lineFollowingThread():
    return threading.Thread(target = followLine)

