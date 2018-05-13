import unittest

from io import StringIO
from unittest import mock

from mission.mission import beginner


def print_info(message):
    return '\x1b[1;34m' + message + '\x1b[0m'


class MissionTest(unittest.TestCase):

    # TODO: params
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_beginner(self, mock_stdout):
        with mock.patch('builtins.input', side_effect=['5 5', '0 0 N', 'MMRMMLMM', '1 0 N', 'MMRMMLMM']):
            beginner()
            result = mock_stdout.getvalue().split('\n')
            assert result[0] == print_info("Plateau confirmed to be 5x5")
            assert result[1] == print_info("Rover deployed at position:	 0 0 N")
            assert result[2] == print_info("Rover is now at position: 2 4 N")
            assert result[3] == print_info("Rover deployed at position:	 1 0 N")
            assert result[4] == print_info("Rover is now at position: 3 4 N")

