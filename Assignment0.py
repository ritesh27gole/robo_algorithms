import numpy as np
import matplotlib.pyplot as plt
import random

grid = np.load('cspace.npy')
print("Grid dimensions are: ", grid.shape)

start = np.array([100.0, 100.0])
goal = np.array([1600.0, 750.0])

goalCircle = plt.Circle((goal[0], goal[1]), 50, color = 'b', fill = False)
fig = plt.figure('RRT Algorithm')
plt.imshow(grid, cmap = 'binary')
plt.plot(start[0], start[1], 'ro')
plt.plot(goal[0], goal[1], 'bo')
ax = fig.gca()
ax.add_patch(goalCircle)
plt.xlabel('X-axis $(m)$')
plt.ylabel('Y-axis $(m)$')


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []
        self.parent = None

def randomPoint():
    x = random.randint(1, grid.shape[1])
    y = random.randint(1, grid.shape[0])
    random_point = np.array([x,y])
    return random_point

first_node = Node(start[0], start[1])

point_1_node = randomPoint()
point_1_node = Node(point_1_node[0], point_1_node[1])
point_2_node = randomPoint()
point_2_node = Node(point_2_node[0], point_2_node[1])

first_node.children.append(point_1_node)
first_node.children[0].children.append(point_2_node)

point_1_node.parent = first_node
point_2_node.parent = point_1_node

def treeTraversal(first_node):
    if not first_node:
        return
    print(first_node.x, first_node.y)
    for children in first_node.children:
        treeTraversal(children)

plt.plot([first_node.x, point_1_node.x, point_2_node.x], [first_node.y, point_1_node.y, point_2_node.y],'go', linestyle="--") 
#traverse tree
print('\nTree nodes')
treeTraversal(first_node)

Waypoint = []
Waypoint.insert(0, start)
Waypoint.append(goal)
print("\n", Waypoint)
plt.show()




