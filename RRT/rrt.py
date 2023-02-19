# Required libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import math

grid = np.load('occupancyGrid.npy')

print("Welcome to implementation of RRT Path Planning Algorithm! \n")
print("The size of current maze (x,y) is: ", grid.shape[1]," X ", grid.shape[0])
start_x = float(input("Enter x coordinate of the starting point: "))
start_y = float(input("Enter y coordinate of the starting point: "))
goal_x = float(input("Enter x coordinate of the goal point: "))
goal_y = float(input("Enter y coordinate of the goal point: "))

start = np.array([start_x, start_y]) #(x,y)
goal = np.array([goal_x, goal_y]) #(x,y)
numIterations = 200
stepSize = 100
goalRegion = plt.Circle((goal[0], goal[1]), stepSize, color='b', fill = False)
startRegion = plt.Circle((start[0], start[1]), stepSize, color='g', fill = False)

fig = plt.figure("RRT Algorithm")
plt.imshow(grid, cmap='binary')
plt.plot(start[0],start[1],'ro')
plt.plot(goal[0],goal[1],'bo')
ax = fig.gca()
ax.add_patch(goalRegion)
ax.add_patch(startRegion)
plt.xlabel('X-axis $(m)$')
plt.ylabel('Y-axis $(m)$')

class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.parent = None
        self.children = []

def randomPoint():
    x = random.randint(1, grid.shape[1])
    y = random.randint(1, grid.shape[0])
    random_point = np.array([x, y])
    return random_point
    

def nearestNode(random_point, Node_list):
    dist = math.inf
    for Node in Node_list:
        node_dist = ((random_point[0] - Node.x)**2 + (random_point[1] - Node.y)**2)**0.5
        if node_dist < dist:
            dist = node_dist
            nearest_node = Node
    return nearest_node


def steeredPoint(nearest_node, random_point, step_size):
    slope = (nearest_node.y - random_point[1])/(nearest_node.x - random_point[0])
    theta = math.atan(slope)
    x = min(int(nearest_node.x + math.cos(theta)*step_size), grid.shape[1] - 1)
    y = min(int(nearest_node.y + math.sin(theta)*step_size), grid.shape[0] - 1)
    x = max(1, x)
    y = max(1, y)
    steered_point = np.array([x, y])
    return steered_point

def checkObstacle(nearest_node, steered_point, step_size):
    intersection = False
    slope = (nearest_node.y - steered_point[1])/(nearest_node.x - steered_point[0])
    theta = math.atan(slope)
    for i in range(1, step_size):
        x = min(int(nearest_node.x + math.cos(theta)*i), grid.shape[1] - 1)
        y = min(int(nearest_node.y + math.sin(theta)*i), grid.shape[0] - 1)
        x = max(1, x)
        y = max(1, y)
        if grid[y][x] == 1:
            intersection = True
            break
        else:
            continue
    return intersection

def retracePath(Node_list):
    solution = []
    goal_node = Node_list[-1]
    solution.append(goal_node)
    parent = goal_node.parent
    while solution[-1] != start_node:
        for Node in Node_list:
            if Node == parent:
                solution.append(Node)
                parent = Node.parent
                break
            else: 
                continue
    return solution

def plotWaypoints():
    previous_node = solution[0]
    for i in range(1, len(solution)):
        next_node = solution[i]
        plt.plot([previous_node.x, next_node.x], [previous_node.y, next_node.y],'go', linestyle="--")
        previous_node = next_node


Node_list = [] # contains (x,y) of each node
start_node = Node(start[0], start[1])
goal_node = Node(goal[0], goal[1])
Node_list.append(start_node) # elements are of Node class
step_size = 100
i = 0

while Node_list[-1].x != goal_node.x and Node_list[-1].y != goal_node.y:
    i += 1

    random_point = randomPoint()
    nearest_node = nearestNode(random_point, Node_list)
    steered_point = steeredPoint(nearest_node, random_point, step_size)
    d = ((steered_point[0] - goal[0])**2 + (steered_point[1] - goal[1])**2)**0.5
    if d <= step_size:
        steered_point = goal
    intersection = checkObstacle(nearest_node, steered_point, step_size)
    if intersection == True:
        continue
    else: 
        steered_node = Node(steered_point[0], steered_point[1])

    steered_node.parent = nearest_node
    nearest_node.children.append(steered_node)
    Node_list.append(steered_node)
    plt.plot(steered_point[0],steered_point[1],'ro')

solution = retracePath(Node_list)
plotWaypoints()
print(start)
plt.show()
