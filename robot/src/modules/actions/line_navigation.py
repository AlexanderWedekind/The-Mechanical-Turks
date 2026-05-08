from modules.state.robot.robot_parts import robotParts
from modules.state.robot.robot_state import robotState
import threading
from modules.state.labyrinth.intersections import Intersection
from modules.actions.drive import DrivingSpeed
drivingSpeed = DrivingSpeed()
from modules.actions.detect_junctions import findJunction

def followLine():
    if robotState['following_line'] == False:
        robotState['following_line'] = True
        while robotState['following_line'] == True:
            drivingSpeed.forwardsLineFollow()
#            if findJunction() != 'no':
                
#    if robotState['following_line'] == False:
#        robotState['following_line'] = True
#        while robotState['following_line'] == True:
#            if robotState['driving'] == False:
#                if robotState['current_speed'] != robotState['driving_speeds']['forwards_line_follow']:
#                    robotState['current_speed'] = robotState['driving_speeds']['forwards_line_follow']
#                robotParts['pirobot'].forward(robotState['current_speed'])
#                robotState['driving'] = True
#            else:
#                if robotState['current_speed'] != robotState['driving_speeds']['forwards_line_follow']:
#                    robotState['current_speed'] = robotState['driving_speeds']['forwards_line_follow']
#                robotParts['pirobot'].forward(robotState['current_speed'])
#            if robotState['road_markings']['middle_sensor'] == True:
#                robotState['current_steering_angle'] = robotState['current_steering_angle'] * -1
#                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])
#            if robotState['road_markings']['left_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
#                robotState['current_steering_angle'] = robotState['steering_angles']['shallow_right']
#                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])
#            if robotState['road_markings']['right_sensor'] == True and robotState['road_markings']['middle_sensor'] == False:
#                robotState['current_steering_angle'] = robotState['steering_angles']['shallow_left']
#                robotParts['pirobot'].set_dir_servo_angle(robotState['current_steering_angle'])
#            if ( robotState['road_markings']['middle_sensor'] == True and robotState['road_markings']['left_sensor'] == True ) or ( robotState['road_markings']['middle_sensor'] == True and robotState['road_markings']['left_sensor'] == True ):
#                if robotState['last_visited_intersection'] == None:
#                    robotState['last_visited_intersection'] = Intersection()
#                    if robotState['bearing'] == 'north':
#                        robotState['last_visited_intersection'].south = 'unexplored_path'
#                    if robotState['bearing'] == 'east':
#                        robotState['last_visited_node'].west = 'unexplored_path'
#                    if robotState['bearing'] == 'south':
#                        robotState['last_visited_node'].north = 'unexplored_path'
#                    if robotState['bearing'] == 'west':
#                        robotState['last_visited_node'].east = 'unexplored_path'
#                elif robotState['bearing'] == 'north':
#                    robotState['last_visited_intersection'].north = Intersection(None, None, robotState['last_visited_intersection'], None)
#                    robotState['last_visited_intersection'] = robotState['last_visited_intersection'].north
#                elif robotState['bearing'] == 'east':
#                    robotState['last_visited_intersection'].east = Intersection(None, None, None, robotState['last_visited_intersection'])
#                    robotState['last_visited_intersection'] = robotState['last_visited_intersection'].east
#                elif robotState['bearing'] == 'south':
#                    robotState['last_visited_intersection'].south = Intersection(robotState['last_visited_intersection'], None, None, None)
#                    robotState['last_visited_intersection'] = robotState['last_visited_intersection'].south
#                elif robotState['bearing'] == 'west':
#                    robotState['last_visited_intersection'].west = Intersection(None, robotState['last_visited_intersection'], None, None)
#                    robotState['last_visited_intersection'] = robotState['last_visited_intersection'].west




def lineFollowingThread():
    return threading.Thread(target = followLine)

