from mission.mission_control import MissionControl


if __name__ == '__main__':
    # TODO: Create integration tests of this file
    print("Welcome to the Mission to mars!")
    mission_control = MissionControl()
    mission_control.scout_plateau()
    mission_control.deploy_rovers()


