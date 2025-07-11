# Ty Davis
# 7/11/2025
# CS 2130
# Dr. Huson
# ---------
# Using Arrays of Data
# filename: hw4.py


from typing import List, Dict
import random

def bubbleSort(A: List[int]):
    "Simple bubble sort implementation"
    i = 0
    didSwap = True
    # Compare to didSwap because if it doesn't swap inside second loop then we're done
    while i < len(A) - 1 and didSwap: 
        didSwap = False
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                didSwap = True
        if not didSwap:
            break

def print_first_last(A: List[int]):
    "Easy function for printing out a beginning and end of an array"
    print('[ ', end='')
    if len(A) > 10:
        for c in A[:5]:
            print(c, end=' ')
        print('...', end='')
        for c in A[-5:]:
            print(c, end=' ')
    print(']')

def main():
    amount: int = 500
    max_val: int = 10000
    random.seed()
    a: List[int] = [random.randint(0, max_val) for _ in range(amount)]
    print("|--------------|")
    print("|   PART ONE   |")
    print("|--------------|")
    print(f"TESTING SORTING ALGORITHM. {amount} random values chosen between 0 and {max_val}.")
    print("BEFORE IT IS SORTED (only a few items shown for brevity):")
    print_first_last(a)
    print("")
    bubbleSort(a)
    print("AFTER IT IS SORTED:")
    print_first_last(a)
    print("")

    print("|--------------|")
    print("|   PART TWO   |")
    print("|--------------|")
    print("TESTING CHARACTER COUNTS")

    # Decided to use a dictionary here because the syntax is just so nice
    letterArray: Dict[str, int] = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

    text = input("Provide a line: ")
    for i in text:
        if i.isalpha():
            # increment the corresponding letter count in the dict if it is alphabetic
            letterArray[i.upper()] += 1

    # easy print all of the counts
    for k, v in letterArray.items():
        print(f"{k} - {v}")


if __name__ == '__main__':
    main()
