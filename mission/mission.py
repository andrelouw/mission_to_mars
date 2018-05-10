from mission.mission_control import MissionControl

if __name__ == '__main__':
    # TODO: Create integration tests of this file
    print("Welcome to the Mission to mars!")
    mission_control = MissionControl()
    mission_control.deploy_rovers(4)

    mission_control.manage_rover(0, 'MRMLMRM')
    rover = mission_control.rovers[0]
    print(f"Rover name is: {rover.name} with position: {rover.get_rover_position()}")

