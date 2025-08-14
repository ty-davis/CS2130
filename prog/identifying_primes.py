# Ty Davis
# Program - Identifying Primes and Euclid's Algorithm with Recursion


def euclid_gcd(val1, val2):
    # if they are equal, we've found our result
    if val1 == val2:
        return val1

    # ensure that val1 is the largest
    if val1 < val2:
        temp = val1
        val1 = val2
        val2 = temp

    # run the algorithm on val1 - val2, and val2
    return euclid_gcd(val1 - val2, val2)

def is_prime(val: int):
    # start at 2 because 1 would always make it True
    i = 2
    is_it_prime = True

    # try only to the sqrt of the val
    while i*i < val:
        if val / i == val // i:
            is_it_prime = False
        i += 1
    return is_it_prime

def main():
    print("This program reads in two integers and determines if they\nare prime. "
         "It then computes the greatest common divisor of\nthe two integers using Euclid's Algorithm.")

    # get the numbers
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))

    # Tell if they are prime
    print(f"{first} is {'not ' if not is_prime(first) else ''}a prime number.")
    print(f"{second} is {'not ' if not is_prime(second) else ''}a prime number.")

    # do euclid if one of the two aren't prime
    if is_prime(first) or is_prime(second):
        gcd_val = 1
    else:
        gcd_val = euclid_gcd(first, second)
    print(f"The gcd({first}, {second}) is {gcd_val}.")

    # ab = gcd(a,b) * lcm(a*b)
    # ab / gcd(a,b) = lcm(a*b)
    lcm_val = first * second // gcd_val
    print(f"The lcm({first}, {second}) is {lcm_val}.")



if __name__ == '__main__':
    main()
