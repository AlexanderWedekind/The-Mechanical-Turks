from robot_hat import Motors 
from picarx import Picarx

def turnOnADime():
    bob = Picarx()
    motors = Motors()

    motors.set_left_reverse()
    bob.set_dir_servo_angle(90)
    motors.forward(50)

    bob.stop()
    motors.stop()
