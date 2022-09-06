"""
Create a python class called DriveBot. Within this class, create instance variables for motor_speed, sensor_range,
and direction. All of these should be initialized to 0 by default. After setting up the class, create an object from
the class called robot_1. Set the motor_speed to 5, the direction to 90, and the sensor_range to 10.
"""

class DriveBot:

    all_disabled = False
    latitude = -999999
    longitude = -999999

    robot_count = 0
    def __init__(self, motor_speed=0, sensor_range=0, direction=0):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot(5, 90, 10)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

test_bot = DriveBot()
test_bot.motor_speed = 30
test_bot.direction = 90
test_bot.sensor_range = 25
print(test_bot.motor_speed)
print(test_bot.direction)
print(test_bot.sensor_range)

# sensor_range defaults
test_bot_1 = DriveBot(10, 270)
print(test_bot_1.direction)
print(test_bot_1.motor_speed)

# direction defaults to 0
test_bot_2 = DriveBot(sensor_range=20, motor_speed=45)
print(test_bot_2.direction)
print(test_bot_2.sensor_range)
print(test_bot_2.motor_speed)

# direction defaults and sensor_range defaults
test_bot_3 = DriveBot(50)
print(test_bot_3.direction)
print(test_bot_3.sensor_range)
print(test_bot_3.motor_speed)

# all default values are used
test_bot_4 = DriveBot()
print(test_bot_4.direction)
print(test_bot_4.sensor_range)
print(test_bot_4.motor_speed)

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)
print(test_bot_5.direction)
print(test_bot_5.sensor_range)
print(test_bot_5.motor_speed)

DriveBot.longitude = -79.98553
DriveBot.latitude = 40.60793
DriveBot.all_disabled = True

robot_6 = DriveBot(35, 75, 25)
robot_7 = DriveBot(20, 60, 10)




