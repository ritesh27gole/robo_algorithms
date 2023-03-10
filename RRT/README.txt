## Rapidly exploring Random Trees (RRT) Algorithm: 
RRT is one of most popular algorithms used for path planning for autonomous vehicles, mobile robots as well as robotic manipulators

Open the "RRT" Folder to find "rrt.py" script and "occupancyGrid.npy" array which resembles a map of room consisting of obstacles

Firstly clone this repository using: 

git clone https://github.com/ritesh27gole/robo_algorithms.git

### Dependencies:
Tested for:  
1. Python (version: 3.8.10)
2. Numpy (version: 1.24.2)
3. Matplotlib (version: 3.7.0)  

You can download the dependencies by entering the following command in terminal:

cd <-path to the RRT folder->
pip install -r requirements.txt

### How to run:
Download the "RRT" folder and copy the path to this folder

In terminal:

cd <-path to the RRT folder->
python3 rrt.py

The pre-loaded occupancy grid can be seen on: https://github.com/ritesh27gole/robo_algorithms/blob/main/README.md

Enter the starting as goal point coordinates when asked, don't put coordinates that would end up on obstacles

After running the script we get a matplotlib plot in which the nodes highlighted by green and blue ring respectively are the start and goal, whereas the dotted green line gives the path found by the algorithm
