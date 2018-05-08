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
    def __init__(self):
        self.name = "athena"
        self.position_x = 0
        self.position_y = 0
        self.direction = 'N'  # TODO: maybe make this enum?
        self.max_x = 10
        self.max_y = 10

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
            print(f'{self.name} is at max y position of {self.max_y}')

    def move_east(self):
        if self.position_x != self.max_x:
            self.position_x += 1
        else:
            print(f'{self.name} is at max x position of {self.max_x}')