from mission.mission_control import MissionControl

if __name__ == '__main__':
    print("Welcome to the Mission to mars!")
    mission_control = MissionControl()
    mission_control.deploy_rovers(4)

    for rover in mission_control.rovers:
        print(f"Rover name is: {rover.name} with position: {rover.get_rover_position()}")
