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


def brief():
    print("-------------------------------------------------------")
    MissionComms.print_bold("""
        Welcome to the Mission to mars!
        
        Brief:
        ------
            You are to deploy rovers to mars and journey the unknown.
        
        Instructions:
        -------------
            -  First you will define the size of the plateau by giving the top x and y coordinates.
                The minimum x and y coordinates are both 0.
            -  To deploy a rover you specify it's coordinates and direction, 
                for example `1 2 N` will deploy a rover at position x = 1 and y = 2 facing North.
            - Valid directions are N, S, E and W.
            - To move a rover you have one of three options:
                - `M` will move the rover forward in the direction it is facing.
                    e.g. Given rover position `0 0 N`: `M` will result in rover position `0 1 N`
                - `R` will rotate the rover 90 degrees clockwise but NOT move it from it's current position.
                    e.g. Given rover position `0 0 N`: `R` will result in rover position `0 0 E`
                - `L` will rotate the rover 90 degrees anti-clockwise but NOT move it from it's current position.
                    e.g. Given rover position `0 0 N`: `L` will result in rover position `0 0 W`
            - Moves can be combined to move the rover, for example:                
                Given rover position `0 0 N`: `MMRMMLM` will result in rover position `2 3 N`
        
        Note on Mission Levels:
        -----------------------
            Two levels were created for this mission, namely Beginner and Advanced.
            - Beginner is the basic assignment use case:
                You deploy a rover at a position and give it coordinates. 
                Once the first rover is moved you moved on the second one. 
                Only 2 rovers are deployed. 
            - Advanced is making things more interesting and interactive. 
                You decide how many rovers you deploy. The maximum is dependent on the size of the plateau.
                They are ll deployed at the bottom of the plateau, next to each other. 
                Once deployed you select the rover you want to move, move it and repeat.
                To quit you just hit Ctrl-C.
                
        Last words:
        -----------
            Try and stay on top of the plateau and don't crash into other rovers.
            May the terminal be with you. 
    """)
    print("-------------------------------------------------------")


if __name__ == '__main__':
    brief()

    print("Mission options: (choose a number)")
    MissionComms.print_bold("----------------------------------")
    MissionComms.print_bold(f"Nr \t| Level \t| Description")
    MissionComms.print_bold("----------------------------------")
    MissionComms.print_bold(f"0 \t| Beginner \t| Deploy one rover at a time (The assignment use case)")
    MissionComms.print_bold(f"1 \t| Advanced \t| Deploy multiple rovers at once (I got carried away...)")

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

    MissionComms.print_pass("Thank you for playing :)")

