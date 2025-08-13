BITSTRING_MAX_SIZE = 10

def get_input(size):
    """Get user input to fill the values of the bitstring"""
    bitstring: int = 0

    if size > BITSTRING_MAX_SIZE or size < 0:
        raise ValueError(f"Size must be between 0 and {BITSTRING_MAX_SIZE}")
    for i in range(size):
        valid = False
        while not valid:
            try:
                new_val = int(input(f"Please enter element {i+1}: "))
                if new_val < 0 or new_val > BITSTRING_MAX_SIZE:
                    raise ValueError(f"Must be between 0 and {BITSTRING_MAX_SIZE}")
                bitstring |= 1 << new_val
                valid = True
            except ValueError as e:
                print(e)
                print("Try again: ", end="")
                valid = False
    return bitstring

def in_bitstring(bitstring, val):
    """True if val in bitstring"""
    return bool((bitstring >> val) & 1)

def display(bitstring: int):
    """Show the bitstring as a string"""
    s = "{ "
    for i in range(BITSTRING_MAX_SIZE):
        if in_bitstring(bitstring, i):
            s += f"{i} "
    s += "}"
    return s


def complement(bitstring):
    """Elements between 0 and BITSTRING_MAX_SIZE that are not in bitstring"""
    new_bitstring = 0
    for i in range(BITSTRING_MAX_SIZE):
        if not in_bitstring(bitstring, i):
            new_bitstring |= 1 << i
    return new_bitstring

def union(bitstring, other_bitstring):
    """Elements in either bitstring or other_bitstring."""
    new_bitstring = 0
    for i in range(BITSTRING_MAX_SIZE):
        if in_bitstring(bitstring, i) or in_bitstring(other_bitstring, i):
            new_bitstring |= 1 << i
    return new_bitstring

def intersection(bitstring, other_bitstring):
    """Elements that are in both bitstring and other_bitstring."""
    new_bitstring = 0
    for i in range(BITSTRING_MAX_SIZE):
        if in_bitstring(bitstring, i) and in_bitstring(other_bitstring, i):
            new_bitstring |= 1 << i
    return new_bitstring

def difference(bitstring, other_bitstring):
    """Elements that are in bitstring but not in other_bitstring."""
    new_bitstring = 0
    for i in range(BITSTRING_MAX_SIZE):
        if in_bitstring(bitstring, i) and not in_bitstring(other_bitstring, i):
            new_bitstring |= 1 << i
    return new_bitstring

def symmetric_difference(bitstring, other_bitstring):
    """Elements that are in bitstring or other_bitstring, but not in both."""
    new_bitstring = 0
    for i in range(BITSTRING_MAX_SIZE):
        if (in_bitstring(bitstring, i) or in_bitstring(other_bitstring, i)) and not (in_bitstring(bitstring, i) and in_bitstring(other_bitstring, i)):
            new_bitstring |= 1 << i
    return new_bitstring


def main():
    a_size = int(input("How many elements in set A: "))
    a = get_input(a_size)

    b_size = int(input("How many elements in set B: "))
    b = get_input(b_size)

    print("                          Set A:", display(a))
    print("                          Set B:", display(b))

    print("                Complement of A:", display(complement(a)))
    print("                Complement of B:", display(complement(b)))

    print("               Union of A and B:", display(union(a, b)))
    print("        Intersection of A and B:", display(intersection(a, b)))
    print("          Difference of A and B:", display(difference(a, b)))
    print("Symmetric Difference of A and B:", display(symmetric_difference(a, b)))


if __name__ == '__main__':
    main()
