#Execution command for question-1: python3 Q1_Josephus_Problem.py

#Execution command for question-2: python3 Q2_8-puzzle_Problem.py 


-----------------------------------------------------   Question-1   -----------------------------------------------------------------------------------------
Python Code: 	Q1_Josephus_Problem.py (code file)

Explanation: 	Josephus Problem statement is implemented in the funtion 'josephus'.
		Values of no.of persons(n) and skip number(k) are taken as input from the terminal.
		conditions: n,k >= 0; else invalid input message will be displayed.
		Creating the list of persons is done by appending the characters by their ASCII values, starting from 65.
		characters are appended one by one in the for loop which runs 'n' times (for n persons). 
		josephus function takes the list of persons and the skip number as arguments of function.
		The person who is going to be killed is given by the index 'idx' through the josephus function.
		'idx = skip_number % len(ls)' This line makes the index not to overflow the range as 
			if skip number > no.of persons, the count again starts from 1st person thinking as the persons are in circular order.
		While loop runs till only 1 person is being survived. 
		In the loop printing of the killed person is done by poping out the persion at the index 'idx' .
		After printing every killed person, the index is updated to 'idx = (idx + skip_number) % len(ls)' .
		The survivor will be the only person left in the list after poping everyone else, i.e, survivor == ls[0].
		for exiting the program when invalid input is given, sys.exit() function is used which is in the sys library, imported at the start of code		


-----------------------------------------------------   Question-2   -----------------------------------------------------------------------------------------
Python Code: 	Q2_8-puzzle_Problem.py (code file)

INPUT	   :	The code takes the input of the Goal State of the puzzle and the initial state of puzzle respectively in the format
		 of a single lined numbers seperated by spaces
		 	e.g: 1 2 3 4 5 6 7 8 0
		 	
Explanation:	input_puzzle() function splits the input puzzle state into a list.
		print_puzzle() function prints the states of the puzzles in the matrix format.
		hv_count() function counts the heuristic value of the given State of the puzzles, which is the value of no.of elements of the 
		State which are mismatched with the final Goal configuration of the puzzle.
		md_count() function finds the manhattan distance of the vertices of the given state of puzzle with the help of state_find() 
		function which finds the position of the number in the matrix format.
		convert() function converts the list format of the State to matrix format of State.
		move() function is the main part of the code where the sum of heuristic value and manhattan distance are compared for the states 
		which are formed by the right,left,up,down movements of the blank slider(0), the state whose sum is small is considered 
		as the next stage of puzzle.
		throught heuristic method we can find the minimum no of moves to get the final Goal state.
		isSolvable() function tells if the puzzle is solvable through the given initial state by finding the no.of inversion pairs.
		in the move() function the current state of the puzzle is stored as duplicate and it is swapped right,left,up,down which are possible
		for the slider to move, this possiblity is checked and written in the while loop at the end of the code.
		pos_idx array stores the possible indices of the puzzle where the slider can be moved.
		Total number of steps required to reach the goal state from the initial state are printing only if the moves are less than 10.
		If the required moves are greater than 10 then it is only shown whether the puzzle is solvable or not.
		sys.maxsize and sys.exit() commands are used from the sys library of python, which is imported at the start of the code.
