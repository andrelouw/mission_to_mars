import unittest

from unittest.mock import patch
from parameterized import parameterized

from mission.rover import Rover


class RoverTest(unittest.TestCase):

    def setUp(self):
        self.rover = Rover("Test Rover", 0, 0, 'N')

    @parameterized.expand([
        ('North', 'N', 'W'),
        ('West', 'W', 'S'),
        ('South', 'S', 'E'),
        ('East', 'E', 'N'),
    ])
    def test_rotate_left(self, name, test_input, expected):
        self.rover.direction = test_input
        self.rover.rotate_left()
        self.assertEquals(self.rover.direction, expected,
                          f'Rotate Left for case "{name}" failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {test_input}')

    @parameterized.expand([
        ('North', 'N', 'E'),
        ('East', 'E', 'S'),
        ('South', 'S', 'W'),
        ('West', 'W', 'N'),
    ])
    def test_rotate_right(self, name, test_input, expected):
        self.rover.direction = test_input
        self.rover.rotate_right()
        self.assertEquals(self.rover.direction, expected,
                          f'Rotate Right for case "{name}" failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {test_input}')

    def test_move_north(self):
        self.rover.move_north()
        self.assertEquals(self.rover.position_y, 1,
                          f'Rover Move north failed.\n'
                          f'Expected:1\n'
                          f'Got: {self.rover.position_y}')

    def test_move_east(self):
        self.rover.move_east()
        self.assertEquals(self.rover.position_x, 1,
                          f'Rover Move east failed.\n'
                          f'Expected: 1\n'
                          f'Got: {self.rover.position_x}')

    def test_move_south(self):
        self.rover.position_y = 1
        self.rover.move_south()
        self.assertEquals(self.rover.position_y, 0,
                          f'Rover Move south failed.\n'
                          f'Expected: 0\n'
                          f'Got: {self.rover.position_y}')

    def test_move_west(self):
        self.rover.position_x = 1
        self.rover.move_west()
        self.assertEquals(self.rover.position_x, 0,
                          f'Rover Move west failed.\n'
                          f'Expected: 0\n'
                          f'Got: {self.rover.position_x}')

    @parameterized.expand([
        ('N', 'mission.rover.Rover.move_north'),
        ('S', 'mission.rover.Rover.move_south'),
        ('E', 'mission.rover.Rover.move_east'),
        ('W', 'mission.rover.Rover.move_west'),
    ])
    def test_move_forward(self, test_input, target):
        with patch(target) as f:
            self.rover.direction = test_input
            self.rover.move_forward()
            f.assert_called()

    def test_get_rover_position(self):
        self.assertEquals(self.rover.get_rover_position(), "0 0 N",
                          f'Get rover position failed.\n'
                          f'Expected: 0 0 N\n'
                          f'Got: {self.rover.get_rover_position()}')
