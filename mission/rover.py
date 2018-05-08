LEFT_ROTATION_MAP = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N',
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
