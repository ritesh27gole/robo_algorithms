import numpy as np

# goal_state = input("Enter the goal state (empty cell as 9): ")
# goal_state = int(goal_state)
# goal_state = [int(i) for i in str(goal_state)]

goal_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

counter = 0
print("\n")
print("The goal state is:")
for i in range(0, len(goal_state)):
    counter += 1
    element = goal_state[i]
    if element == 9:
        element = "X"
    if (counter % 3 == 0):
        print(element, end = "  ")
        print("\n")
    else:
        print(element, end = "  ")

final_index = 8                                                                             # Index of number 9 i.e. the blank spot in the above array

# initial_state = input("Enter the starting state that you want to solve (empty cell as 9): ")
# initial_state = int(initial_state)
# initial_state = np.array([int(i) for i in str(initial_state)])

initial_state = np.array([7, 2, 4, 5, 9, 6, 8, 3, 1])

print("\n")
print("The initial state is:")
for i in range(0, len(initial_state)):
    counter += 1
    element = initial_state[i]
    if element == 9:
        element = "X"
    if (counter % 3 == 0):
        print(element, end = "  ")
        print("\n")
    else:
        print(element, end = "  ")

# Solvability Checker
initial_index = None                                                                        # Initialzing the index of number 9 i.e. the blank spot in the above array
initial_inversions = []

for i in range(0,len(initial_state)):
    current_number = initial_state[i]

    if current_number == 9:
        initial_index = i

    current_inversions = 0

    for j in range(i, len(initial_state)):
        if current_number > initial_state[j]:
            current_inversions += 1

    initial_inversions.append(current_inversions)

total_inversions = sum(initial_inversions)

parity = (final_index - initial_index) % 2

if (total_inversions % 2 == parity):
    print("The given initial state is SOLVABLE! \n")
else: 
    print("The given initial state is NOT SOLVABLE!")
    exit()

# Solver
initial_matrix = np.resize(initial_state, (3,3))
goal_matrix = np.resize(goal_state, (3,3))

inequality_matrix = (initial_matrix != goal_matrix).astype(int)
h_initial = np.sum(inequality_matrix)
print("Initial h cost: ", h_initial, "\n")

solved = 0 
g_initial = 0
g = 0

solution = []
initial_step = [g_initial, h_initial, initial_state]
solution.append(initial_step)

mem_matrix = np.zeros((3,3))

while solved != 1:
    previous_state = solution[g][2]
    previous_matrix = np.resize(previous_state, (3,3))

    if g > 0:
        mem_matrix = np.resize(solution[g-1][2], (3,3))

    print("Previous Matrix is:")
    print(previous_matrix, "\n")

    dir_possible = []    # Possible directions
    nine_coord = (np.where(previous_matrix == 9)[0][0], np.where(previous_matrix == 9)[1][0])

    for i in range(nine_coord[0] - 1, nine_coord[0] + 2):
        delta_i = abs(i - nine_coord[0])
        for j in range(nine_coord[1] - 1, nine_coord[1] + 2):
            delta_j = abs(j - nine_coord[1])
            dir_flag = (i < 3 and i >= 0 and j < 3 and j >= 0 and (delta_i + delta_j == 1))
            if dir_flag == True:
                dir_possible.append((i,j))
            else:
                continue
    
    h = 9
    for dir in dir_possible:
        step = []
        cache = previous_matrix.copy()
        current_matrix = cache
        current_matrix[nine_coord[0], nine_coord[1]] = current_matrix[dir[0], dir[1]]
        current_matrix[dir[0], dir[1]] = 9
        if (current_matrix == mem_matrix).all() == True:
            continue
        print(current_matrix, "\n")
        inequality_matrix = (current_matrix != goal_matrix).astype(int)
        h_current = np.sum(inequality_matrix)
        if h_current < h:
            h = h_current
            step.append(current_matrix)
            # print(step, "\n")
        elif h_current == h:
            print("Waimt!")
            print(step)
            exit()
    
    g += 1
    print("Step " + str(g) + " is:")
    print(step, "\n")
    current_step = [g, h, np.resize(step, (3,3))]
    solution.append(current_step)

    if (current_matrix == goal_matrix).all() == True:
        solved = 1

# print("Directions possible are: ", dir_possible, "\n")
# print(current_matrix)
