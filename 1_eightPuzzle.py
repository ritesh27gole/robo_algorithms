goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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

initial_state = input("Enter the starting state that you want to solve (empty cell as 9): ")
initial_state = int(initial_state)
initial_state = [int(i) for i in str(initial_state)]

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
    print("The given initial state is SOLVABLE!")
else: 
    print("The given initial state is NOT SOLVABLE!")

