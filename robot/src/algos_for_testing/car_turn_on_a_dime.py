from robot_hat import Motors 
from picarx import Picarx

bob = Picarx()
motors =Motors()

def turnOnADime():
    motors.set_left_reverse()
    bob.set_dir_servo_angle(90)
    motors.forward(50)
