import pandas as pd
import math
import sys

sys.set_int_max_str_digits(0)

memo = {}

def format_large_number(x):
    """Formats a number into a string with scientific notation."""
    if isinstance(x, str):
        return x
    if isinstance(x, float):
        return f"{x:.6e}"
    if not isinstance(x, int):
        return x

    # Handle integers that can be safely converted to float
    if abs(x) < 1e7:
        return str(x)
    if abs(x) < 1e308:
        return f"{float(x):.6e}"

    # Handle very large integers manually
    s = str(x)
    sign = ""
    if s.startswith('-'):
        sign = "-"
        s = s[1:]
    
    exponent = len(s) - 1
    mantissa = f"{s[0]}.{s[1:7]}"
    return f"{sign}{mantissa}e+{exponent}"

def factorial(n):
    return math.factorial(n)

def fibonacci(n):
    print(n)
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibonacci2(n):
    print(n)
    # if n > 1000:
    #     return "really big"
    global memo
    # include memoization
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    else:
        val = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = val
        return val

def main():
    n_axis = [5, 10, 20, 50, 100, 1000, 10000, 1000000]
    functions = {
        "lg n": lambda n: math.log(n),
        "n": lambda n: n,
        "n lg n": lambda n: n * math.log(n),
        "n^2": lambda n: n * n,
        "n^3": lambda n: n * n * n,
        "fib b": lambda n: fibonacci(n),
        "2^n": lambda n: 2 ** n,
        "3^n": lambda n: 3 ** n,
        "n!": lambda n: factorial(n),
    }

    data = {name: [func(n) for n in n_axis] for name, func in functions.items()}
    df = pd.DataFrame(data, index=n_axis)

    # df = pd.DataFrame(vals_big, columns=list(functions.keys()))
    df = df.applymap(lambda x: format_large_number(x))
    df.to_csv("out.csv")
    with open('out.txt', 'w') as fout:
        fout.write(df.to_string())



if __name__ == '__main__':
    main()
