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
