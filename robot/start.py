from picarx import Picarx
import time

px = Picarx()
speed = 30
stop = 0
backUp = 15
turnNow = 30


def main():
    while True:
        distance = round(px.ultrasonic.read(), 2)
        if distance < turnNow:
            px.forward(stop)
            speed = 5
            if distance < backUp:
                speed = 10
                while distance < backUp:
                    px.backward(speed)
                speed = 5
            while distance < turnNow:
                px.set_dir_servo_angle(30)
                px.forward(speed)
        px.forward(speed)
    

