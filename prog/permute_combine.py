# Ty Davis
# Counting: Permutations and Combinations
# CS2130 - Dr. Huson
# 8/14/2025

import math

def permutations(n, x):
    "n! / (n-x)!"
    return math.factorial(n) // math.factorial(n-x)

def combinations(n, x):
    "n! / ((n-x)! x!)"
    return math.factorial(n) // math.factorial(n-x) // math.factorial(x)


def main():
    print("Testing the permutation and combination functions:")
    print("6 choose 6", combinations(6, 6))
    print("6 permute 6", permutations(6, 6))
    print("30 choose 6", combinations(30, 6))
    print("10 permute 5", permutations(10, 5))

    doc_1 = combinations(12, 4)
    nur_1 = combinations(36, 12)
    doc_nur_1 = doc_1 * nur_1
    print("Ways of selecting doctors for the first batch:", doc_1)
    print("Ways of selecting nurses for the first batch:", nur_1)
    print("Ways to administer the first dose:", doc_nur_1)
    print("")

    doc_2 = combinations(8, 4)
    nur_2 = combinations(24, 12)
    doc_nur_2 = doc_2 * nur_2
    print("Ways of selecting doctors for the second batch:", doc_2)
    print("Ways of selecting nurses for the second batch:", nur_2)
    print("Ways to administer the second dose:", doc_nur_2)

    print( "Total number of ways to administer all doses:")
    print( " 12 choose 4 * 36 choose 12   *   8 choose 4 * 24 choose 12   *   4 choose 4 * 12 choose 12")
    print(f" {doc_nur_1:,} * {doc_nur_2:,} * 1")
    print(f"The numeric answer is: {doc_nur_1 * doc_nur_2:,}")

    print("The number of ways to distribute 4 bonuses to 23 people is: ", permutations(23, 4))
    print("If the bonuses are the same, there are: ", combinations(23, 4))


if __name__ == '__main__':
    main()
