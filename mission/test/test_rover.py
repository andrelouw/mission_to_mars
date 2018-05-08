import unittest
from parameterized import parameterized
from mission.rover import Rover


class RoverTest(unittest.TestCase):

    def setUp(self):
        self.rover = Rover()

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

    @parameterized.expand([
        ('Move if not max', 0, 1),
        ('Move if max', 10, 10),
    ])
    def test_move_north(self, name, test_input, expected):
        self.rover.position_y = test_input
        self.rover.move_north()
        self.assertEquals(self.rover.position_y, expected,
                          f'{name} failed.\n'
                          f'Expected: {expected}\n'
                          f'Got: {self.rover.position_y}')
