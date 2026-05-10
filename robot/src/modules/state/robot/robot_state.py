class SteeringAngles:
    def __init__(self):
        self.sharpRight = 45
        self.sharpLeft = 45
        self.shallowRight = 15
        self.shallowLeft = 15

class DrivingSpeeds:
    def __init__(self):
        self.stopped = 0
        self.forwards = 30
        self.reverse = 10
        self.forwardsLineFollow = 25
        self.reverseLineFollow = 5
        self.cornering = 15

OLDrobotState = {
        'driving': False,
        'current_speed': 0,
        'current_steering_angle': 0,
        'road_clear': True,
        'closing_down': True,
        'watching_road_markings': False,
        'was_used_watch_road_markings': False,
        'read_distance_timeout': 0.02,
        'distance': 0,
        'watching_distance': False,
        'was_used_watch_distance': False,
        'line_found': False,
        'is_on_line': False,
        'is_following_line': False,
        'read_road_markings_timeout': 0.02,
        'changed_road_markings': False,
        'grayscale_sensitivity': 400,
        'grayscale_threshold_margin': 0.3,
        'road_markings': [
                [False, False, False],
             ],
        'junction_detect_time_interval': 1,
        'driving_speeds': {
            'stopped': 0,
            'forwards': 30,
            'reverse': 10,
            'forwards_line_follow': 25,
            'reverse_line_follow': 5,
            'cornering': 15,
            },
        'steering_angles': {
            'sharp_right': 45,
            'shallow_right': 15,
            'sharp_left': -45,
            'shallow_left': -15,
            },
        'last_visited_intersection': None,
        'bearing': 'north',
        }

class RobotState:
    def __init__(self):
        self.driving = False
        self.currentSpeed = 0
        self.currentSteeringAngle = 0
        self.roadClear = True
        self.closingDown = True
        self.watchingRoadMarkings = False
        self.wasUsedWatchRoadMarkings = False
        self.readDistanceTimeout = 0.02
        self.distance = 0
        self.watchingDistance = False
        self.wasUsedWatchDistance = False
        self.isOnLine = False
        self.isFollowingLine = False
        self.readRoadMarkingsTimeout = 0.02
        self.changedRoadMarkings = False
        self.grayscaleSensitivity = 400
        self.grayscaleThresholdMargin = 0.3
        self.roadMarkings = [
            [False, False, False],
        ]
        self.junctionDetectTimeInterval = 1
        self.drivingSpeeds = DrivingSpeeds()
        self.steeringAngles = SteeringAngles()
        self.lastVisitedJunction = None
        self.bearing = 'north'

robotState = RobotState()
