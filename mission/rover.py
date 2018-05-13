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
    def __init__(self, name: str, start_x: int, start_y: int, direction: str) -> None:
        self.name = name
        self.position_x = start_x
        self.position_y = start_y
        self.direction = direction
        self.min_x = 0
        self.min_y = 0

    def rotate_left(self):
        # use maps as no case switch in python
        self.direction = LEFT_ROTATION_MAP[self.direction]

    def rotate_right(self):
        # use maps as no case switch in python
        self.direction = RIGHT_ROTATION_MAP[self.direction]

    def move_north(self):
        self.position_y += 1

    def move_east(self):
        self.position_x += 1

    def move_south(self):
        self.position_y -= 1

    def move_west(self):
        self.position_x -= 1

    def move_forward(self):
        if self.direction == 'N':
            self.move_north()
        elif self.direction == 'E':
            self.move_east()
        elif self.direction == 'S':
            self.move_south()
        elif self.direction == 'W':
            self.move_west()

    def get_rover_position(self) -> str:
        return f"{self.position_x} {self.position_y} {self.direction}"
