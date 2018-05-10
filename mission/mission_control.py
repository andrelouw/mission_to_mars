from mission.rover import Rover
from mission.comms import MissionComms


ROVER_NAMES = {
    0: 'Athena',
    1: 'Betty',
    2: 'Constance',
    3: 'Delta'
}


class MissionControl:
    def __init__(self):
        self.rovers = []
        self.max_x = 0
        self.max_y = 0

    def deploy_rovers(self):
        number_of_rovers = input("Number of rovers (1-4) to deploy? ")
        if number_of_rovers.isdigit():
            if int(number_of_rovers) > 4:
                MissionComms.print_fail("Can't deploy more than 4 rovers!")
                self.deploy_rovers()
            if int(number_of_rovers) <= 0:
                MissionComms.print_fail("We need some rovers, choose a number between 1 and 4")
                self.deploy_rovers()
            for rover in range(int(number_of_rovers)):
                rover = Rover(ROVER_NAMES[rover], 0, 0, self.max_x, self.max_y)
                self.rovers.append(rover)
                MissionComms.print_info(f"Rover {rover.name} deployed with position:\t {rover.get_rover_position()}")
        else:
            MissionComms.print_fail("Expecting a number between 1 and 4")
            self.deploy_rovers()

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

    def scout_plateau(self):
        size = input("How big is the plateau? ")
        max_coordinates = size.split()
        self.max_x = max_coordinates[0]
        self.max_y = max_coordinates[1]
        MissionComms.print_info(f"Plateau confirmed to be {self.max_x}x{self.max_y}")


