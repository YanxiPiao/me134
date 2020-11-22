class Joint:
    def __init__(self, board, channel, minPulse, maxPulse, startAngle):
        self.board = board
        self.channel = channel
        self.minPulse = minPulse
        self.maxPulse = maxPulse
        self.startAngle = startAngle
        self.currAngle = self.startAngle


JOINT1 = Joint(0, 0, 600, 2500, 135)
JOINT2 = Joint(0, 1, 575, 2500, 135)
JOINT3 = Joint(0, 2, 600, 2500, 90)
JOINT4 = Joint(0, 3, 550, 2500, 135)
JOINT5 = Joint(0, 4, 550, 2500, 135)
JOINT6 = Joint(0, 5, 700, 2500, 90)
JOINT7 = Joint(0, 6, 700, 2500, 135)
JOINT8 = Joint(0, 7, 600, 2500, 135)
JOINT9 = Joint(0, 8, 500, 2500, 90)
JOINT10 = Joint(1, 0, 750, 2500, 135)
JOINT11 = Joint(1, 1, 700, 2500, 135)
JOINT12 = Joint(1, 2, 500, 2600, 90)
JOINT13 = Joint(1, 3, 500, 2500, 135)
JOINT14 = Joint(1, 4, 700, 2500, 135)
JOINT15 = Joint(1, 5, 500, 2500, 90)
JOINT16 = Joint(1, 6, 500, 2500, 135)
JOINT17 = Joint(1, 7, 600, 2500, 135)
JOINT18 = Joint(1, 8, 600, 2500, 90)


class Leg:
    def __init__(self, foot, knee, shoulder):
        self.foot = foot
        self.knee = knee
        self.shoulder = shoulder
        self.joints = [foot, knee, shoulder]


LEG1 = Leg(JOINT1, JOINT2, JOINT3)
LEG2 = Leg(JOINT4, JOINT5, JOINT6)
LEG3 = Leg(JOINT7, JOINT8, JOINT9)
LEG4 = Leg(JOINT10, JOINT11, JOINT12)
LEG5 = Leg(JOINT13, JOINT14, JOINT15)
LEG6 = Leg(JOINT16, JOINT17, JOINT18)

LEGS = [LEG1, LEG2, LEG3, LEG4, LEG5, LEG6]
