# Ty Davis
# Homework 7
# CS2130 - Dr. Huson
# Converting an algorithm into code


def main():
    # main loop
    while True:
        # get the user's input
        num = int(input("Please enter an integer to determine the prime factorization of: "))

        # make sure num > 2
        if num < 2:
            print("Number should be above 2")
            continue

        # the factorization algorithm
        k = num
        i = 2
        # test until the square root of num
        while i*i < num:
            # keep dividing while the remainder is 0
            while (k % i == 0):
                print(i)
                k = k // i
            i += 1
        # don't print k if it is 1 because 1 is implied
        if (k > 1):
            print(k)

        # ask the user if they want to go again
        again = 'y' in input("Would you like to try again? (y or n) ").lower()
        if not again:
            break

if __name__ == '__main__':
    main()
