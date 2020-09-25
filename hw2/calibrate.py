import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit2 = ServoKit(channels=16, address=0x41)

kit.servo[0].angle = 0
time.sleep(1)
kit.servo[0].angle = 180
