# The Mars Rover Technical Challenge.
This is my implementation for the [marsrovertechchallenge](https://code.google.com/archive/p/marsrovertechchallenge/) .

## TL;DR
Clone the repo and ensure you have [python](https://www.python.org/) version 3.6.0 installed as well as https://pypi.org/project/pip/.

To launch the mission run `make run` in the root of the project and follow the prompts.


## Launch
### Run
To launch the mission, open up the terminal and run:
`make run`

###  Instructions:
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

### Mission Levels
Two levels were created for this mission, namely Beginner and Advanced.
- Beginner is the basic assignment use case:
    - You deploy a rover at a position and give it coordinates.
    - Once the first rover is moved you moved on the second one.
    - Only 2 rovers are deployed.
- Advanced is making things more interesting and interactive.
    - You decide how many rovers you deploy. The maximum is dependent on the size of the plateau.
    - They are ll deployed at the bottom of the plateau, next to each other.
    - Once deployed you select the rover you want to move, move it and repeat.
    - To quit you just hit Ctrl-C.


## Other goodies

### Tests
To run tests: `make test`
This command will install some dependencies we need to run the tests.
After installation all test will run.

### Collision avoidance
The idea of rovers landing/running into each other or falling of the plateau is frightening. To prevent this **collision avoidance** feature was introduced.
The **collision avoidance** feature does the following:
- Prevents rovers from being deployed on top of each other
- Prevents rovers from running into each other
- Prevents rovers from falling of the plateau
If a collision is immanent, being with a fellow rover or the abyss, the rover will stop at it's current position and not move forward.
All remaining commands will be aborted and the user will be notified of this action.

### A note on virtual environments
A **Virtual Environment** and **pyenv** was used during the development of this project.
When running this project it is strongly recommended to also run it in a virtual environment.
More on this can be found here:
- [Virtual Environments](https://virtualenv.pypa.io/en/stable/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)


## Last words
Some of the original ideas did not make it into this project due to the lack of time. But for completeness sake I include the outstanding work here:
- Create more tests for edge cases being catered for in the code.
- Add simple docstrings for each method and class explaining what it does etc.



