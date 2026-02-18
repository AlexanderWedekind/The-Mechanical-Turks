from picarx import Picarx

bob = Picarx()

def measureDistance():
    distance = bob.ultrasinic.read()
    print('-- distance measured: ' + str(distance))
    return distance


