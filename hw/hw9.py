# Ty Davis
# Fibonacci performance - Recursion vs Iteration
# CS2130 - Dr. Huson
# 8/14/25

import timeit

def fibo_r(n):
    # recursive solution
    if n < 2:
        return n
    return fibo_r(n-1) + fibo_r(n-2)

def fibo_i(n):
    # initial conditions
    fib = 0
    n2 = 1
    n1 = 1
    if n < 2:
        return n

    # iterative solution
    for _ in range(2,n):
        fib = n1 + n2
        n2 = n1
        n1 = fib
    return fib

def main():
    n = int(input("Please enter a value to determine the Fibonacci sequence element for: "))

    # use timeit to see how long each version takes
    r_time = timeit.timeit(lambda: print(f"The value computed recursively is {fibo_r(n)}"), number=1)
    i_time = timeit.timeit(lambda: print(f"The value computed iteratively is {fibo_i(n)}"), number=1)

    print(f"Recursive Fibonacci({n}) Time: {r_time:.6f} seconds")
    print(f"Iterative Fibonacci({n}) Time: {i_time:.6f} seconds")


if __name__ == '__main__':
    main()
