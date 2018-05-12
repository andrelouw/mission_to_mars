from mission.comms import MissionComms
from mission.mission_control import MissionControl


def beginner():
    mission_control = MissionControl()
    mission_control.scout_plateau()
    mission_control.deploy_rover()
    mission_control.deploy_rover()


def advanced():
    mission_control = MissionControl()
    mission_control.scout_plateau()
    mission_control.deploy_rovers()
    while True:
        mission_control.drive_rovers()


if __name__ == '__main__':
    # TODO: Create integration tests of this file
    # TODO: Explainer text
    print("Welcome to the Mission to mars!")

    print("Mission options:")
    print("----------------------------------")
    print(f"Nr \t| Level \t| Description")
    print("----------------------------------")
    print(f"0 \t| Beginner \t| Deploy one rover at a time (The assignment use case)")
    print(f"1 \t| Advanced \t| Deploy multiple rovers at once (I got carried away...)")

    while True:
        try:
            l = input()
            level = int(l)
            if 0 <= level < 2:
                break
        except ValueError:
            pass

        MissionComms.print_warn("Expecting a number, 0 or 1")
        continue

    if level is 0:
        beginner()
    elif level is 1:
        advanced()

    print("Thank you for playing :)")

