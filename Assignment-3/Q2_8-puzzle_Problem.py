# Python code for Q2. 8 Puzzle Problem

import sys

# Taking the input of the puzzle state
def input_puzzle():
    inp_puzzle = list(map(int, input().split()))

    matrix = []
    for i in range(9):
        matrix.append(inp_puzzle[i])
    return matrix

# Printing the puzzle states in matrix format
def print_puzzle(matrix):
    print("\t",end="")
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("\n\t",end="")
        print(matrix[i], " ", end="")

# Converting list to matrix
def convert(s):
    mat = []
    a = []
    b = []
    c = []
    for i in range(9):
        if i<3:
            a.append(s[i])
        if i>=3 and i<=5:
            b.append(s[i])
        if i>5:
            c.append(s[i])

    mat.append(a)
    mat.append(b)
    mat.append(c)
    return mat

# Counting the heuristic value of a state of the 8 puzzle
def hv_count(s):
    count = 0
    goal = goal_state

    # Loop that iterates through all the tiles of unsolved puzzle and compares them with
    # the solved one's. if they don't match, then increase the heuristic value count by 1
    for i in range(9):
        if s[i] != 0 and s[i] != goal[i]:
            count += 1
    return count

# Counting the manhattan distance of a state of the 8 puzzle

def state_find(val):
    x1 = sys.maxsize
    y1 = sys.maxsize
    ideal = conv_goal
    for i in range(3):
        for j in range(3):
            if ideal[i][j] == val:
                x1 = i
                y1 = j
                break
    return x1, y1

def md_count(state):
    con_state = conv_state
    x1 = y1 = x2 = y2 = sys.maxsize
    total_h = 0
    for i in range(3):
        for j in range(3):
            x1, y1 = state_find(con_state[i][j])
            x2, y2 = i, j
            total_h += abs(x1-x2)+abs(y1-y2)
    return total_h

# The movement function that moves the blank tile to possible positions
# and compares the moved states for the minimum heuristic valued state
visited_states=[]

def move(array, position, state):

    # variable to store the minimum heuristic value of a moved state
    rel_h = sys.maxsize
    rel_hv = sys.maxsize

    # Copying the puzzle state to another list variable
    store_state = state.copy()

    # Loop that makes moves of blank tiles to all possible positions
    for i in range(len(array)):

        # Copying the current puzzle state to another list variable to be
        # used in the swapping blank tile operation
        duplicate_state = state.copy()

        # swapping the blank tile
        duplicate_state[position], duplicate_state[pos_idx[i]] = duplicate_state[pos_idx[i]], duplicate_state[position]

        # counting the heuristic values for swaped puzzle state
        tmp_hv = hv_count(duplicate_state)
        tmp_md = md_count(duplicate_state)
        tmp_h = tmp_hv + tmp_md
	
        # if current swaped puzzle state has the less total heuristic value than
        # the before one, then store current state and current total heuristic value
        if tmp_h < rel_h and duplicate_state not in visited_states:
            rel_h = tmp_h
            rel_hv = tmp_hv
            store_state = duplicate_state.copy()
    # return the state with the minimum heuristic value along with the heuristic value
    visited_states.append(store_state)
    return store_state, rel_hv, rel_h

# Solved state of a 8 puzzle
print("Enter the Goal State:")
goal_state = input_puzzle()	#goal state in list form
conv_goal = convert(goal_state)	#goal state in matrix form

# Unsolved 8 Puzzle stored in list 'state'
print("Enter the Initial State:")
state = input_puzzle()		#initial state in list form
conv_state = convert(state)	#initial state in matrix form

# Check if the puzzle is solvable
def isSolvable(arr):
    inv_count = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if arr[j] != 0 and arr[i] != 0 and arr[i] > arr[j]:
                inv_count += 1
    return (inv_count % 2 == 0)


if (isSolvable(state) + isSolvable(goal_state)) % 2 == 1 :
	sys.exit("Not Solvable")
else:
	print("Solvable")
# variable that stores the heuristic value
misplaced_n = hv_count(state)

# Keeps track of search levels
Steps = 0

# initial printing of current state of 8 puzzle
print("\nInitial State of the puzzle is:\n")
print_puzzle(state)
print()

# The main loop to find the solution and printing every search level
while misplaced_n > 0:
    if Steps >= 10:
    	sys.exit("\nGoal State will be reached but takes more than 10 steps...")
    # Store the position of the blank tile labeled '0' in the list 'state'
    pos = state.index(0)

    # Increasing level as one level of search is executing now
    Steps += 1

    # if blank tile is in index 0, then possible movement operation
    if pos == 0:
        # array of indexes where blank tile can be moved
        pos_idx = [1, 3]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 2, then possible movement operation
    elif pos == 2:
        # array of indexes where blank tile can be moved
        pos_idx = [1, 5]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 8, then possible movement operation
    elif pos == 8:
        # array of indexes where blank tile can be moved
        pos_idx = [5, 6]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 1, then possible movement operation
    elif pos == 1:
        # array of indexes where blank tile can be moved
        pos_idx = [0, 2, 4]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 3, then possible movement operation
    elif pos == 3:
        # array of indexes where blank tile can be moved
        pos_idx = [0, 4, 6]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 5, then possible movement operation
    elif pos == 5:
        # array of indexes where blank tile can be moved
        pos_idx = [2, 4, 8]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 6, then possible movement operation
    elif pos == 6:
        # array of indexes where blank tile can be moved
        pos_idx = [3, 7]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 7, then possible movement operation
    elif pos == 7:
        # array of indexes where blank tile can be moved
        pos_idx = [4, 6, 8]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # if blank tile is in index 4, then possible movement operation
    elif pos == 4:
        # array of indexes where blank tile can be moved
        pos_idx = [1, 3, 5, 7]
        state, misplaced_n, fval = move(pos_idx, pos, state)

    # print current state and heuristic of that state in each search level
    print("\n------- Step",Steps,"---------\n")
    print_puzzle(state)
    print()

print("\nGoal State reached!")
print("Total no.of moves needed :",Steps)
