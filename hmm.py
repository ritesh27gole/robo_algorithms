# Helper function to find the index of an element in a list
def find_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i

# Helper function to swap two elements in a list
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# Heuristic function: count the number of misplaced tiles
def misplaced_tiles(state):
    count = 0
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range(9):
        if state[i] != goal_state[i]:
            count += 1
    return count

# Solvability Checker:
def solvability_checker(initial_state):
    final_index = 8
    initial_index = None
    final_index = 8
    initial_inversions = []

    for i in range(0,len(initial_state)):
        current_number = initial_state[i]

        if current_number == 0:
            initial_state[i] = 9
            initial_index = i

        current_inversions = 0

        for j in range(i, len(initial_state)):
            if current_number > initial_state[j]:
                current_inversions += 1

        initial_inversions.append(current_inversions)

        if initial_state[i] == 9:
            initial_state[i] = 0

    total_inversions = sum(initial_inversions)

    parity = (final_index - initial_index) % 2

    if (total_inversions % 2 == parity):
        print("The given initial state is SOLVABLE! \n")
    else: 
        print("The given initial state is NOT SOLVABLE!")
        exit()


# A* algorithm to solve the 8-puzzle problem and return the sequence of moves and states
def astar(start_state):
    visited = set()
    heap = [(misplaced_tiles(start_state), start_state, 0, None)]
    while heap:
        heap.sort()
        (h, state, moves, parent) = heap.pop(0)
        if state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            path = [(state, moves)]
            while parent is not None:
                (state, moves, parent) = parent
                path.append((state, moves))
            return path[::-1]  
        visited.add(tuple(state))
        blank_index = find_index(state, 0)
        if blank_index != 0 and blank_index != 3 and blank_index != 6:
            # Move the tile to the left
            new_state = state.copy()
            swap(new_state, blank_index, blank_index - 1)
            if tuple(new_state) not in visited:
                heap.append((misplaced_tiles(new_state) + moves + 1, new_state, moves + 1, (state, moves, parent)))
        if blank_index != 0 and blank_index != 1 and blank_index != 2:
            # Move the tile up
            new_state = state.copy()
            swap(new_state, blank_index, blank_index - 3)
            if tuple(new_state) not in visited:
                heap.append((misplaced_tiles(new_state) + moves + 1, new_state, moves + 1, (state, moves, parent)))
        if blank_index != 2 and blank_index != 5 and blank_index != 8:
            # Move the tile to the right
            new_state = state.copy()
            swap(new_state, blank_index, blank_index + 1)
            if tuple(new_state) not in visited:
                heap.append((misplaced_tiles(new_state) + moves + 1, new_state, moves + 1, (state, moves, parent)))
        if blank_index != 6 and blank_index != 7 and blank_index != 8:
            # Move the tile down
            new_state = state.copy()
            swap(new_state, blank_index, blank_index + 3)
            if tuple(new_state) not in visited:
                heap.append((misplaced_tiles(new_state) + moves + 1, new_state, moves + 1, (state, moves, parent)))
    return []

# Example usage
start_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]  
solvability_checker(start_state)
num_moves = astar(start_state)
if num_moves == -1:
    print("Unsolvable puzzle")
else:
    print(f"Solved the puzzle in {num_moves} moves")
