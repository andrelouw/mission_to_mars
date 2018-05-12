from mission.comms import MissionComms


class CommandAbort(Warning):
    def __init__(self, message):
        MissionComms.print_warn(message)

        super().__init__(message)
