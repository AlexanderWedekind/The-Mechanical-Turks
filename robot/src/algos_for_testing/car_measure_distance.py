from picarx import Picarx


def MeasureDistance():
    bob = Picarx()
    distance = bob.ultrasonic.read()
    print('-- distance measured: ' + str(distance))
    bob.stop()
    return distance


