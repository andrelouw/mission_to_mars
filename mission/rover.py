from mission.comms import MissionComms


LEFT_ROTATION_MAP = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N',
}

RIGHT_ROTATION_MAP = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}


class Rover:
    def __init__(self, name: str, start_x: int, start_y: int, max_x: int, max_y: int):
        self.name = name
        self.position_x = start_x
        self.position_y = start_y
        self.direction = 'N'  # TODO: maybe make this enum?
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = 0
        self.min_y = 0

    def rotate_left(self):
        # use maps as no case switch in python
        self.direction = LEFT_ROTATION_MAP[self.direction]

    def rotate_right(self):
        # use maps as no case switch in python
        self.direction = RIGHT_ROTATION_MAP[self.direction]

    def move_north(self):
        if self.position_y != self.max_y:
            self.position_y += 1
        else:
            MissionComms.print_warn(f'{self.name} is at max y position of {self.max_y}')

    def move_east(self):
        if self.position_x != self.max_x:
            self.position_x += 1
        else:
            MissionComms.print_warn(f'{self.name} is at max x position of {self.max_x}')

    def move_south(self):
        if self.position_y != self.min_y:
            self.position_y -= 1
        else:
            MissionComms.print_warn(f'{self.name} is at min y position of {self.min_y}')

    def move_west(self):
        if self.position_x != self.min_x:
            self.position_x -= 1
        else:
            MissionComms.print_warn(f'{self.name} is at min x position of {self.min_x}')

    def move_forward(self):
        if self.direction == 'N':
            self.move_north()
        elif self.direction == 'E':
            self.move_east()
        elif self.direction == 'S':
            self.move_south()
        elif self.direction == 'W':
            self.move_west()

    def get_rover_position(self):
        return f"{self.position_x} {self.position_y} {self.direction}"
