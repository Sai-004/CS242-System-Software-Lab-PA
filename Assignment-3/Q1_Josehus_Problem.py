# Python code for Q1. Josephus Problem

import sys

# josephus function implementation
def josephus(ls, skip_number):

    # Storing the index of the person to be killed
    idx = skip_number % len(ls)
    
    # Runs the loop until only 1 person is survived
    while len(ls) > 1:
    	# Printing the killer
    	print(ls[idx-(skip_number % len(ls))], end=" kills ")
    	# Killing the person at idx
    	print(ls.pop(idx))
    	# Updating the index for killing
    	idx = (idx + skip_number) % len(ls)
    
    # Printing out the Survivor
    print("\nSurvivor : ", ls[0])
# end of the josephus function

# Taking the input data of no_of persons and the skip number
n=int(input("Enter the no_of persons (n): "))
if n<=0:
	sys.exit("!!! n cannot be non-positive !!!\n")

k=int(input("Enter the skip number (k): "))
if k<0:
	sys.exit("!!! k cannot be negative !!!\n")
print()

# Creating the list of Persons [A,B,C,....]
persons=[]
for i in  range(65,n+65):
    	persons.append(chr(i))

# Function calling for the Output
josephus(persons,k)
