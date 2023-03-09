# Algorithms in Robotics

General software problems in robotics solved using fundamental algorithms

## Rapidly exploring Random Trees (RRT) Algorithm: 
RRT is one of most popular algorithms used for path planning for autonomous vehicles, mobile robots as well as robotic manipulators

Open the "RRT" Folder to find "rrt.py" script and "occupancyGrid.npy" array which resembles a map of room consisting of obstacles

Firstly clone this repository using: 
```
git clone https://github.com/ritesh27gole/robo_algorithms.git
```

### Dependencies:
Tested for:  
1. Python (version: 3.8.10)
2. Numpy (version: 1.24.2)
3. Matplotlib (version: 3.7.0)  <br>

You can download the dependencies by entering the following command in terminal
```
cd <-path to the RRT folder->
pip install -r requirements.txt
```
### How to run:
Download the "RRT" folder and copy the path to this folder

In terminal:
```
cd <-path to the RRT folder->
python3 rrt.py
```
This is the pre-loaded occupancy grid:
![occupancy_grid](https://user-images.githubusercontent.com/83658560/224113730-060295bc-104b-4c03-aedf-8b9c7153cd7b.png)

Enter the starting as goal point coordinates as shown below, don't put coordinates that would end up on obstacles
![terminal_screenshot](https://user-images.githubusercontent.com/83658560/219943849-a6565287-da28-412a-aaa6-1d8381c1a60c.png)

After running the script we get:
![RRT_Algorithm](https://user-images.githubusercontent.com/83658560/224113898-400425ee-2370-4e71-b093-557bdf042f01.png)
Here nodes highlighted by green and blue ring respectively are the start and goal, whereas the dotted green line gives the path found by the algorithm

## Eight puzzle solver using A* algorithm:

Comparison of different heuristics used:
![Figure_1](https://user-images.githubusercontent.com/83658560/224112173-110c2ebc-870a-4845-a384-28b3f1e2525c.png)



