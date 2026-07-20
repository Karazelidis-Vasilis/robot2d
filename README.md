# Robot2D
## Purpose
    My goal is to build my own autonomous lawnmower. To achieve this, I divided the project into a series of smaller projects, each focusing on a specific software engineering or robotics concept. This is the start of series of robotics projects where I am building my software engineering skills. 
## About this project 
    My first step is to make a small project using python, gain some experience. Step by step I will add to my skillset NumPy, kinematics, control and ROS 2 and make new project for each of them.
# Description 
    Robot2D is a simple command-line simulation of a differential-drive robot developed as the first project of my robotics software engineering roadmap. The user interacts with the program by entering single-letter commands. User will be able to move the robot,rotate it, see robots current position and orientation, see history of previous position and plot robots route on Matplot. Also user can input text file with commands by input files path, this file must have one word and one number in each line like the text file in this repository.
## Features 
    - Input validation
    - Command file parser
    - Pose history
    - Trajectory plotting with Matplotlib
    - Angle normalization to [-180°, 180°]
    - Error handling
    - `if __name__ == "__main__"` entry point
## How to run
    Clone the repository and run the Python file:
    python main.py

## How project works   
    By running the programme, it will ask the user to input a specific letter. Each letter is responsible for specific action:
    - m will ask to input number(distance) to move the robot
    - r will ask to input number(degree) to rotate the robot
    - s to show current pose, dimentions and orientation
    - h to show every point that robot passed
    - p to simulate the robots route on Matplot
    - f will ask to input path of a text file, to read commands from there, the text file must  - - consist by lines with one word(move or rotate and a number)
    - q will stop the programme
## Example
    When the user will run this file, it will ask for input(m,r,s,h,p,f and q). So user can do this:
    - m
    - Distance: 2
    - s
    -Current position X:2.0 Y:0.0
    -Current angle 0.0
    - h
    -Point 0 : (0.0 0.0)
    -Point 1 : (2.0 0.0)
    -q
    -Exit from Meny.
    -Good bye!!!

## What I learned
    In my opinions this project was good practice for my skills python. I used:
    - Classes
    - while loop
    - for loop
    - if statement
    - try expect
    - split()
    - import libraries
    - simple math operations
    - If main == name
    - read files
    - Matplot
## Next project
    This project is finished and will not receive new features.
    The next step of my roadmap is a NumPy-based Robot2D implementation.
## Roadmap
    |    Topics      | Status    |
    |----------------|-----------|    
    | Python         | Completed |
    | NumPy          |   Next    |
    | Kinematics     |  Planned  |
    | Planning       |  Planned  |
    | Control        |  Planned  |
    | ROS 2          |  Planned  |
    | Computer Vision|  Planned  |
    | Navigation     |  Planned  |

    The roadmap may change in the future.
    