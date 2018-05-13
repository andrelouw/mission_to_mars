from mission.error import RoverError
from mission.rover import Rover
from mission.comms import MissionComms
from mission.warning import CommandAbort

ROVER_NAMES = {
    0: 'Anna',
    1: 'Bettie',
    2: 'Cotie',
    3: 'Didi'
}


class MissionControl:
    def __init__(self):
        self.rovers = []
        self.max_x = 0
        self.max_y = 0

    def scout_plateau(self):
        while True:
            size = input(f"\nHow big is the plateau?\nFor example: `5 5`\n")
            max_coordinates = size.split()
            try:
                self.max_x = int(max_coordinates[0])
                self.max_y = int(max_coordinates[1])
                if self.max_x == 0 or self.max_y == 0:
                    MissionComms.print_warn("We can do better than that, make the plateau bigger than 0")
                    continue
                MissionComms.print_info(f"Plateau confirmed to be {self.max_x}x{self.max_y}")
                break
            except (IndexError, ValueError):
                MissionComms.print_warn("Expecting 2 coordinates separated by a space, for example: 5 5")
                continue

    def deploy_rover(self):
        prompt = "\nWhere should the rover be deployed?\n" if len(self.rovers) == 0 \
            else "\nWhere should the next rover be deployed?\n"
        while True:
            try:
                coordinates = input(prompt).split()
                x = int(coordinates[0])
                y = int(coordinates[1])
                d = coordinates[2].upper()
                if d not in ['N', 'S', 'E', 'W']:
                    MissionComms.print_warn(f"Not a valid direction, options are N, S, E, and W")
                    continue
                if x > self.max_x or y > self.max_y:
                    MissionComms.print_warn(f"Not a valid position, try and keep it in bounds")
                    continue
                rover = Rover("Rover", x, y, d)
                self.collision_avoidance(rover, deployment=True)
                break
            except (ValueError, IndexError):
                MissionComms.print_warn(f"Expecting 2 numbers and a direction in the format: 0 0 N")
                continue
            except RoverError:
                MissionComms.print_warn(f"A rover is already deployed there, try again.")
                continue

        MissionComms.print_info(f"{rover.name} deployed at position:\t {rover.get_rover_position()}")
        self.rovers.append(rover)
        self._drive_rover(rover)

    def deploy_rovers(self):
        max_rovers = 4 if self.max_x > 4 else self.max_x
        while True:
            number_of_rovers = input(f"\nNumber of rovers (1-{max_rovers}) to deploy?\n")
            if number_of_rovers.isdigit():
                if int(number_of_rovers) > max_rovers:
                    MissionComms.print_fail(f"Can't deploy more than {max_rovers} rovers!")
                    continue
                if int(number_of_rovers) <= 0:
                    MissionComms.print_fail("We need some rovers, choose a number between 1 and 4")
                    continue
                break
            MissionComms.print_fail(f"Expecting a number between 1 and {max_rovers}")
            continue

        for r in range(int(number_of_rovers)):
            rover = Rover(ROVER_NAMES[r], r, 0, 'N')
            self.rovers.append(rover)
            MissionComms.print_info(f"Rover {rover.name} deployed at position:\t {rover.get_rover_position()}")

    def _drive_rover(self, rover: Rover):
        commands = input(f"\nWhat are the commands for the rover?\n")
        self._manage_rover(rover, commands)

    def drive_rovers(self):
        print("")
        print("Which rover would you like to give orders to? (choose a number)")
        MissionComms.print_bold("----------------------------------")
        MissionComms.print_bold(f"Nr \t| Name  \t| Position")
        MissionComms.print_bold("----------------------------------")
        for index, rover in enumerate(self.rovers):
            MissionComms.print_bold(f"{index} \t| {rover.name}  \t| {rover.get_rover_position()}")

        while True:
            try:
                index = int(input())
                if 0 <= index < len(self.rovers):
                    break
            except ValueError:
                pass

            MissionComms.print_warn(f"Please provide a valid number between 0 and {len(self.rovers) - 1}")

        rover = self.rovers[index]
        commands = input(f"\nPlease enter commands for {rover.name}:\n")
        self._manage_rover(rover, commands)

    def _manage_rover(self, rover: Rover, commands: str):
        for command in list(commands):
            try:
                self._action_command(command, rover)
            except CommandAbort:
                break
        MissionComms.print_info(f"{rover.name} is now at position: {rover.get_rover_position()}")

    def _action_command(self, command: str, rover):
        command = command.upper()
        if command == 'L':
            rover.rotate_left()
        elif command == 'R':
            rover.rotate_right()
        elif command == 'M':
            try:
                self.collision_avoidance(rover)
                rover.move_forward()
            except RoverError:
                raise CommandAbort("Aborting commands")
        else:
            MissionComms.print_warn(f"{command} is not a valid command, ignoring this command.")

    def collision_avoidance(self, rover, deployment=False):
        if self._is_end_of_plateau(rover):
            raise RoverError(f"{rover.name} is at the end of the plateau!")
        for r in self.rovers:
            if self._is_in_path(rover, r, deployment):
                raise RoverError(f"Crash imminent, {r.name} already located at {r.position_x} {r.position_y}!")

    @staticmethod
    def _is_in_path(rover1: Rover, rover2: Rover, deployment=False) -> bool:
        width = 0 if deployment else 1
        if rover1.direction == 'N':
            if rover1.position_x == rover2.position_x and (rover1.position_y + width) == rover2.position_y:
                return True
        if rover1.direction == 'E':
            if (rover1.position_x + width) == rover2.position_x and rover1.position_y == rover2.position_y:
                return True
        if rover1.direction == 'S':
            if rover1.position_x == rover2.position_x and (rover1.position_y - width) == rover2.position_y:
                return True
        if rover1.direction == 'W':
            if (rover1.position_x - width) == rover2.position_x and rover1.position_y == rover2.position_y:
                return True

        return False

    def _is_end_of_plateau(self, rover) -> bool:
        if rover.direction == 'N':
            if rover.position_y + 1 == self.max_y + 1:
                return True
        if rover.direction == 'E':
            if rover.position_x + 1 == self.max_x + 1:
                return True
        if rover.direction == 'S':
            if rover.position_y - 1 == -1:
                return True
        if rover.direction == 'W':
            if rover.position_x - 1 == -1:
                return True

        return False
