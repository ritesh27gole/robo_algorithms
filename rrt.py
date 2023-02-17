import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Define the class for the nodes in the tree
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

# Define the function to generate a random point within the workspace
def get_random_point(x_limit, y_limit):
    x = random.uniform(0, x_limit)
    y = random.uniform(0, y_limit)
    return Node(x, y)

# Define the function to find the nearest node in the tree to a given point
def get_nearest_node(tree, point):
    nearest_node = None
    min_distance = float("inf")
    for node in tree:
        distance = math.sqrt((node.x - point.x)**2 + (node.y - point.y)**2)
        if distance < min_distance:
            nearest_node = node
            min_distance = distance
    return nearest_node

# Define the function to extend the tree towards a given point
def extend_tree(node, new_node, max_distance):
    distance = math.sqrt((node.x - new_node.x)**2 + (node.y - new_node.y)**2)
    if distance > max_distance:
        x = node.x + (new_node.x - node.x) * max_distance / distance
        y = node.y + (new_node.y - node.y) * max_distance / distance
        return Node(x, y)
    else:
        return new_node

# Define the RRT function
def RRT(start, goal, x_limit, y_limit, max_distance, max_iter):
    tree = [start]
    for i in range(max_iter):
        random_point = get_random_point(x_limit, y_limit)
        nearest_node = get_nearest_node(tree, random_point)
        new_node = extend_tree(nearest_node, random_point, max_distance)
        if new_node is not None:
            new_node.parent = nearest_node
            tree.append(new_node)
            if math.sqrt((new_node.x - goal.x)**2 + (new_node.y - goal.y)**2) <= max_distance:
                goal.parent = new_node
                tree.append(goal)
                return tree
    return None

# Define the function to visualize the tree and the path
def visualize(tree, start, goal, x_limit, y_limit):
    plt.figure()
    for node in tree:
        if node.parent is not None:
            plt.plot([node.x, node.parent.x], [node.y, node.parent.y], 'k-', lw=1)
    plt.plot(start.x, start.y, 'ro', markersize=5)
    plt.plot(goal.x, goal.y, 'go', markersize=5)
    if goal.parent is not None:
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = node.parent
        path.reverse()
        for i in range(len(path)-1):
            plt.plot([path[i].x, path[i+1].x], [path[i].y, path[i+1].y], 'r-', lw=2)
    plt.axis([0, x_limit, 0, y_limit])
    plt.show()

# Define the workspace limits
x_limit = 10
y_limit = 10

# Define the start and goal nodes
start = Node(1, 1)
goal = Node(9, 9)

# Define the maximum distance between nodes and the maximum number of iterations
max_distance = 1
max_iter = 10000

# Run the RRT algorithm and visualize the result
tree = RRT(start, goal, x_limit, y_limit, max_distance, max_iter)
if tree is not None:
    visualize(tree, start, goal, x_limit, y_limit)
else:
    print("Path not found")
