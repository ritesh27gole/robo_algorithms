import numpy as np

class Node:
    def __init__(self, state, f = None, h = None):
        self.state = state
        self.f = f
        self.h = h
        self.parent = None
        self.children = []

def initialization():
    goal_state = input("Enter the goal state (empty cell as 9): ")
    goal_state = int(goal_state)
    goal_state = [int(i) for i in str(goal_state)]

    counter = 0
    print("\n")
    print("The goal state is:")
    for i in range(0, len(goal_state)):
        counter += 1
        element = goal_state[i]
        if element == 9:
            element = "_"
        if (counter % 3 == 0):
            print(element, end = "  ")
            print("\n")
        else:
            print(element, end = "  ")
    print("---------------------------------------------")

    initial_state = input("Enter the starting state that you want to solve (empty cell as 9): ")
    initial_state = int(initial_state)
    initial_state = np.array([int(i) for i in str(initial_state)])

    print("\n")
    print("The initial state is:")
    for i in range(0, len(initial_state)):
        counter += 1
        element = initial_state[i]
        if element == 9:
            element = "_"
        if (counter % 3 == 0):
            print(element, end = "  ")
            print("\n")
        else:
            print(element, end = "  ")
    print("---------------------------------------------")

    return initial_state, goal_state

def checkSolvability(initial_state, goal_state):
    flag = False
    for i in range(0,len(goal_state)):
        if goal_state[i] == 9:
            goal_index = i

    initial_inversions = 0
    for i in range(0,len(initial_state)):
        if initial_state[i] == 9:
            initial_index = i

        for j in range(i, len(initial_state)):
            if initial_state[i] > initial_state[j]:
                initial_inversions += 1

    parity = (goal_index - initial_index) % 2

    if (initial_inversions % 2 == parity):
        print("The given initial state is SOLVABLE! \n")
        flag = True
    else: 
        print("The given initial state is NOT SOLVABLE!")
        exit()

    return flag

def possibleMoves(state):
    state_matrix = np.resize(state, (3,3))
    dir_possible = []    # Possible directions
    nine_coord = (np.where(state_matrix == 9)[0][0], np.where(state_matrix == 9)[1][0])

    for i in range(nine_coord[0] - 1, nine_coord[0] + 2):
        delta_i = abs(i - nine_coord[0])
        for j in range(nine_coord[1] - 1, nine_coord[1] + 2):
            delta_j = abs(j - nine_coord[1])
            dir_flag = (i < 3 and i >= 0 and j < 3 and j >= 0 and (delta_i + delta_j == 1))
            if dir_flag == True:
                dir_possible.append((i,j))
            else:
                continue

    return dir_possible

def misplacedTileHeuristic(state):
    h = 0
    inequality = (state != goal_state).astype(int)
    h = np.sum(inequality)
    return h

def retracePath(Node_list):
    solution = []
    goal_node = Node_list[-1]
    start_node = Node_list[0]
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

def solution_moves(solution):
    print("The moves to the solution are as follows: \n")

    for i in range(0, len(solution)):
        counter = 0
        next_node = solution[len(solution)-1-i]
        next_state = next_node.state
        for i in range(0, len(next_state)):
            counter += 1
            element = next_state[i]
            if element == 9:
                element = "_"
            if (counter % 3 == 0):
                print(element, end = "  ")
                print("\n")
            else:
                print(element, end = "  ")
        print("---------------------------------------------")

    for i in range(0, len(goal_state)):
        counter += 1
        element = goal_state[i]
        if element == 9:
            element = "_"
        if (counter % 3 == 0):
            print(element, end = "  ")
            print("\n")
        else:
            print(element, end = "  ")

initial_state, goal_state = initialization()
solvability = checkSolvability(initial_state, goal_state)

g = 0
h = misplacedTileHeuristic(initial_state)
f = g + h

open = []
initial_node = Node(initial_state, f, h)
open.append(initial_node)

closed = []

k=0
while (open[-1].state == goal_state).all() == False:
    previous_node = open[-1]
    closed.append(open.pop())
    moves = possibleMoves(previous_node.state)
    previous_f = previous_node.f
    previous_h = previous_node.h
    previous_g = previous_f - previous_h
    g = previous_g + 1

    for move in moves:
        step = []
        cache = previous_node.state.copy()
        current_state = cache
        nine_coord = int(np.where(current_state == 9)[0])
        current_state[nine_coord] = current_state[3*move[0] + move[1]]
        current_state[3*move[0] + move[1]] = 9
        flag_open = False
        flag_closed = False
        for i in range(0, len(open)):
            if (current_state == open[i].state).all() == True:
                flag_open = True
                break
            else:
                continue
        
        for i in range(0, len(closed)):
            if (current_state == closed[i].state).all() == True:
                flag_closed = True
                break
            else:
                continue
        
        if (flag_open == True) or (flag_closed == True):
            continue
        else:
            h = misplacedTileHeuristic(current_state)
            f = g + h
            current_node = Node(current_state, f, h)
            current_node.parent = previous_node
            open.append(current_node)
    
    open = sorted(open, key= lambda x: (x.f, x.h), reverse=True)

solution = retracePath(closed)
solution_moves(solution)
