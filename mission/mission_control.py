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

    def deploy_rovers(self, number_of_rovers):
        for rover in range(number_of_rovers):
            self.rovers.append(Rover(ROVER_NAMES[rover]))

