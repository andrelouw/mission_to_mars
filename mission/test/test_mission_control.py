import unittest
from parameterized import parameterized
from mission.mission_control import MissionControl, ROVER_NAMES


class RoverTest(unittest.TestCase):

    def setUp(self):
        self.mission_control = MissionControl()

    def test_deploy_rovers(self):
        self.mission_control.deploy_rovers(4)
        self.assertEquals(len(self.mission_control.rovers), 4)
        for index, rover in enumerate(self.mission_control.rovers):
            self.assertEquals(rover.name, ROVER_NAMES[index])

    @parameterized.expand([
        ('Left', 'N', 'L', '0 0 W'),
        ('Right', 'N', 'R', '0 0 E'),
        ('Move', 'N',  'M', '0 1 N'),
    ])
    def test_action_command_left(self, name, test_iput, command, expected):
        self.mission_control.deploy_rovers(1)
        rover = self.mission_control.rovers[0]
        rover.direction = test_iput
        rover.position_x = 0
        rover.position_y = 0

        MissionControl._action_command(command, rover)
        self.assertEquals(rover.get_rover_position(), expected,
                          f'Action Command {name} failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {rover.get_rover_position()}')

    def test_manage_rover(self):
        self.mission_control.deploy_rovers(1)
        self.mission_control.manage_rover(0, 'MRML')
        rover = self.mission_control.rovers[0];
        self.assertEquals(rover.get_rover_position(), '1 1 N')

