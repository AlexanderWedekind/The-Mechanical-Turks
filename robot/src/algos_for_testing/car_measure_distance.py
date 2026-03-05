from picarx import Picarx

bob = Picarx()

def MeasureDistance():
    distance = bob.ultrasonic.read()
    print('-- distance measured: ' + str(distance))
    return distance


