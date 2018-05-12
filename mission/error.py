from mission.comms import MissionComms


class RoverError(Exception):
    def __init__(self, message):
        MissionComms.print_fail(message)

        super().__init__(message)
