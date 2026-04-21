from modules.hardware_startup import robotParts

def turnOnADime():

    robotParts['motors'].set_left_reverse()
    robotParts['pirobot'].set_dir_servo_angle(90)
    robotParts['motors'].forward(50)

