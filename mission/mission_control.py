from mission.rover import Rover


ROVER_NAMES = {
    0: 'Athena',
    1: 'Betty',
    2: 'Constance',
    3: 'Delta'
}


class MissionControl:
    def __init__(self):
        self.rovers = []

    def deploy_rovers(self, number_of_rovers: int):
        for rover in range(number_of_rovers):
            self.rovers.append(Rover(ROVER_NAMES[rover]))

    def manage_rover(self, index: int, commands: str):
        rover = self.rovers[index]
        for command in list(commands):
            self._action_command(command, rover)

    @staticmethod
    def _action_command(command: str, rover: Rover):
        if command == 'L':
            rover.rotate_left()
        elif command == 'R':
            rover.rotate_right()
        elif command == 'M':
            rover.move_forward()
