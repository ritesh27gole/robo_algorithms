# Algorithms in Robotics

General software problems in robotics solved using fundamental algorithms

## Rapidly exploring Random Trees (RRT) Algorithm: 
RRT is one of most popular algorithms used for path planning for autonomous vehicles, mobile robots as well as robotic manipulators

Open the "RRT" Folder to find "rrt.py" script and "occupancyGrid.npy" array which resembles a map of room consisting of obstacles

### Dependencies:
Tested for:  
1. Python (version: 3.8.10)
2. Numpy (version: 1.24.2)
3. Matplotlib (version: 3.7.0)  <br>

You can download the dependencies by entering the following command in terminal
```
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
![occupancy_grid](https://user-images.githubusercontent.com/83658560/219943838-73637cb4-1019-4958-8207-e05cd6491abc.png)

Enter the starting as goal point coordinates as shown below, don't put coordinates that would end up on obstacles

![terminal_screenshot](https://user-images.githubusercontent.com/83658560/219943849-a6565287-da28-412a-aaa6-1d8381c1a60c.png)
