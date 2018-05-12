import unittest
import pytest
from unittest.mock import patch
from parameterized import parameterized

from mission.error import RoverError
from mission.mission_control import MissionControl, ROVER_NAMES
from mission.rover import Rover


class MissionControlTest(unittest.TestCase):

    def setUp(self):
        self.mission_control = MissionControl()
        self.mission_control.max_x = 10
        self.mission_control.max_y = 10

        with patch('builtins.input', side_effect='2'):
            self.mission_control.deploy_rovers()

    def test_deploy_rovers(self):
        # TODO: Cases for when exception has to be raised
        self.mission_control.rovers = []
        with patch('builtins.input', side_effect='4'):
            self.mission_control.deploy_rovers()
            self.assertEquals(len(self.mission_control.rovers), 4)
            for index, rover in enumerate(self.mission_control.rovers):
                self.assertEquals(rover.name, ROVER_NAMES[index])

    def test_manage_rover(self):
        self.mission_control.manage_rover(0, 'MRML')
        rover = self.mission_control.rovers[0]
        self.assertEquals(rover.get_rover_position(), '1 1 N')

    @parameterized.expand([
        ('Left', 'N', 'L', '0 0 W'),
        ('Right', 'N', 'R', '0 0 E'),
        ('Move', 'N',  'M', '0 1 N'),
    ])
    def test_action_command(self, name, test_input, command, expected):
        rover = self.mission_control.rovers[0]
        rover.direction = test_input
        rover.position_x = 0
        rover.position_y = 0
        self.mission_control._action_command(command, rover)
        self.assertEquals(rover.get_rover_position(), expected,
                          f'Action Command {name} failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {rover.get_rover_position()}')

    def test_scout_plateau(self):
        user_input = ['15 20']
        with patch('builtins.input', side_effect=user_input):
            self.mission_control.scout_plateau()

        self.assertEquals(self.mission_control.max_x, 15)
        self.assertEquals(self.mission_control.max_y, 20)

    def test_collision_avoidance(self):
        with pytest.raises(RoverError):
            self.mission_control.manage_rover(1, "MLM")
            self.mission_control.manage_rover(0, 'M')

    @parameterized.expand([
        ('False', 'N', 1, 1, False),
        ('North', 'N', 1, 2, True),
        ('South', 'S', 1, 0, True),
        ('East', 'E', 2, 1, True),
        ('West', 'W', 0, 1, True),
        ('EdgeN', 'N', 0, 2, False),
        ('EdgeS', 'S', 0, 0, False),
        ('EdgeE', 'E', 2, 0, False),
        ('EdgeW', 'W', 0, 0, False),
    ])
    def test_is_in_path(self, name, direction, r2x, r2y, expected):
        rover1 = Rover("Rover 1", 1, 1, 10, 10)
        rover1.direction = direction
        rover2 = Rover("Rover 2", r2x, r2y, 10, 10)

        result = MissionControl._is_in_path(rover1, rover2)
        self.assertEquals(result, expected,
                          f'Test in path {name} failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {result}')


