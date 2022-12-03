# Python code for Q1. Minimun no.of Denominations
import sys

# Function for computing the minimun no.of denominations

def minDenominations(V):
    currency = [50, 25, 20, 10, 5, 1]		# Types of coins taken as list
    n = len(currency)
    ans = [0] * (6)				# List for storing no.of coins of each type
    coins = 0					# Total no.of coins
    for i in range(n):				# Loop for counting the denominations
        while (V >= currency[i]):
            V -= currency[i]
            ans[i] = ans[i] + 1
            coins = coins+1

    return coins, ans				# Function returns two types of variables at a time

def minDenominations_25(V):
    currency = [50, 20, 10, 5, 1]		# Types of coins taken as list
    n = len(currency)
    ans = [0] * (5)				# List for storing no.of coins of each type
    coins = 0					# Total no.of coins
    for i in range(n):				# Loop for counting the denominations
        while (V >= currency[i]):
            V -= currency[i]
            ans[i] = ans[i] + 1
            coins = coins+1

    return coins, ans				# Function returns two types of variables at a time

# Input of the amount
amount = int(input("Enter the amount required: "))

# Function calling
denominations, currencylist = min(
    minDenominations(amount), minDenominations_25(amount))

# Printing no.of denominations of each type of coins
print("No of coins required: ", denominations)
if (len(currencylist) == 6):
    print("No of 50 coins:\t", currencylist[0])
    print("No of 25 coins:\t", currencylist[1])
    print("No of 20 coins:\t", currencylist[2])
    print("No of 10 coins:\t", currencylist[3])
    print("No of 5 coins:\t", currencylist[4])
    print("No of 1 coins:\t", currencylist[5])
else:
    print("No of 50 coins:\t", currencylist[0])
    print("No of 25 coins:\t 0")
    print("No of 20 coins:\t", currencylist[1])
    print("No of 10 coins:\t", currencylist[2])
    print("No of 5 coins:\t", currencylist[3])
    print("No of 1 coins:\t", currencylist[4])

