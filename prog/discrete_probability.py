# Ty Davis
# Discrete Probability: Working with large and small populations
# CS2130 - Dr. Huson
# 8/14/25


import math

def permutations(n, x):
    "n! / (n-x)!"
    return math.factorial(n) // math.factorial(n-x)

def combinations(n, x):
    "n! / ((n-x)! x!)"
    return math.factorial(n) // math.factorial(n-x) // math.factorial(x)

def binomial(n, k, p):
    "p^k (1-p)^(n-k)"
    return p ** k * (1 - p) ** (n - k) * combinations(n, k)

def main():
    print("60 cars at a dealer, 3 dead batteries. If we check 10, what is "
          "the probability no more than 1 will have a dead battery?")
    a = 0
    for x in [0, 1]:
        # can't use bernoulli here because trials and dependent
        N = 60
        K = 3
        n = 10
        p = 0.05
        a += (combinations(K, x) * combinations(N - K, n - x)) / combinations(N, n)
    print(f"Probability is: {a:.6}")

    print("Auto recall: 8% have defect. If we test 20, what is"
          "probability that at most 2 will have the defect?")

    a = 0
    for k in [0, 1, 2]:
        # bernoulli works because trials and independent
        n = 20
        p = 0.08
        a += binomial(n, k, p)
    print(f"Probability is: {a:.6}")



    
if __name__ == '__main__':
    main()
