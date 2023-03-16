## Eight puzzle solver using A* algorithm:

### Solvability

We first find the amount of moves required to move the blank from position in initial state to position in goal state. We the find if the number of moves are even or odd. This is called the "parity" of the puzzle. Then we find the sum of total number of inversions and find whether it is even or odd, this is said to be the parity of initial state. If both the puzzle parity and initial state parity are same, that means the puzzle is solvable, otherwise it is not solvable.

### Comparison of different heuristics used (tested for 10 puzzles)

![comparison](https://user-images.githubusercontent.com/83658560/225425739-179e558b-09cb-44e6-aa2a-4763e7e14d96.png)

The sample states and the time taken by each heuristic is given in the results.txt file
