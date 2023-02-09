initial_state = input("Enter the starting state that you want to solve: ")
initial_state = int(initial_state)
initial_state = [int(i) for i in str(initial_state)]
initial_inversions = []

for i in range(0,len(initial_state)):
    current_number = initial_state[i]
    current_inversions = 0
    for j in range(i, len(initial_state)):
        if current_number > initial_state[j]:
            current_inversions += 1
    initial_inversions.append(current_inversions)

total_inversions = sum(initial_inversions)

if (total_inversions % 2 == 0):
    print("The given initial state is SOLVABLE!")
else: 
    print("The given initial state is NOT SOLVABLE!")

