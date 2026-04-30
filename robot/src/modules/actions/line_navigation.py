from modules.hardware_startup import robotParts
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
                robotstate['driving'] = True
            else:
                if robotstate['current_speed'] != robotState['driving_speeds']['forwards_line_follow']:
                    robotState['current_speed'] = robotstate['driving_speeds']['forwards_line_follow']
                robotParts['pirobot'].forward(robotState['current_speed'])
            if robotState['road_markings']['middle_sensor'] == True:
                robotParts['pirobot'].set_dir_servo_angle(0)
            if robotState['road_markings']['left_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
                robotParts['pirobot'].set_dir_servo_angle(robotState['steering_angles']['shallow_right'])
            if robotState['road_markings']['right_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
                robotParts['pirobot'].set_dir_servo_angle(robotState['steering_angles']['shallow_left'])

