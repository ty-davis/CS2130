# Ty Davis
# Fibonacci and Summation
# CS2130 - Dr. Huson
# 8/14/2025

def fibo(n, memo={}):
    # Gonna use memoization to make it faster on big numbers, and prevent recursion depth limits
    if n in memo:
        return memo[n]

    # the first 2 fibonacci
    if n < 2:
        memo[n] = n
        return n
    else:
        # recursive fibonacci solution
        memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
        return memo[n]


def summation(n):
    if n == 1:
        return 1

    # recursive solution because it is fun
    return n + summation(n-1)


def main():
    try:
        n_f = int(input("Enter a number for which to compute fibonacci: "))
        print(f"Fibonacci of {n_f}:", fibo(n_f))
    except ValueError as e:
        print(e)
        print("Try again.")
        return

    try:
        n_s = int(input("Enter a number for which to compute the summation: "))
        sum = summation(n_s)
        print(f"Summation of {n_s}:", sum)

        # report if the summation is correct according to the formula
        if sum == n_s * (n_s + 1) / 2:
            print("The summation and formula were the same.")
        else:
            print("The summation and formula were not the same.")
    except ValueError as e:
        print(e)
        print("Try again.")
        return

if __name__ == '__main__':
    main()
