# Ty Davis
# 7/10/2025
# CS 2130
# Dr. Huson
# Encoding data with bits: Sets and Set Operations
from typing import Self

class Bitstring:
    """A class to represent the bitstring"""
    max_size: int = 10
    max_num:  int = max_size - 1

    def __init__(self, my_set: int = 0):
        """Add the value to the set"""
        self._my_set: int = my_set   # the integer representation of the set itself

    def _add_to_set(self, val: int):
        """Add the val to self"""
        self._my_set |= 1 << val

    def get_input(self, size) -> None:
        """Get user input to fill the values of the set"""
        if size > Bitstring.max_size or size < 0:
            raise ValueError(f"Size must be between 0 and {Bitstring.max_size}")
        for i in range(size):
            valid = False
            while not valid:
                try:
                    new_val = int(input(f"Please enter element {i+1}: "))
                    if new_val < 0 or new_val > Bitstring.max_num:
                        raise ValueError(f"Must be between 0 and {Bitstring.max_size}")
                    self._add_to_set(new_val)
                    valid = True
                except ValueError as e:
                    print(e)
                    print("Try again: ", end="")
                    valid = False

    def __str__(self) -> str:
        s = "{ "
        for i in range(Bitstring.max_size):
            if self._in_set(i):
                s += f"{i} "
        s += "}"
        return s

    def _in_set(self, val: int) -> bool:
        """True if val is in self"""
        return bool((self._my_set >> val) & 1)

    @property
    def _size(self) -> int:
        """The number of elements in the self (cardinality)"""
        size = 0
        for i in range(Bitstring.max_size):
            if self._in_set(i):
                size += 1
        return size

    def complement(self):
        """Elements between 0 and max_num that are not in self"""
        new_set = Bitstring()
        for i in range(Bitstring.max_size):
            if not self._in_set(i):
                new_set._add_to_set(i)
        return new_set

    def union(self, other_set: Self):
        """Elements in either self or other_set."""
        new_set = Bitstring()
        for i in range(Bitstring.max_size):
            if self._in_set(i) or other_set._in_set(i):
                new_set._add_to_set(i)
        return new_set

    def intersection(self, other_set: Self):
        """Elements that are in both self and other_set."""
        new_set = Bitstring()
        for i in range(Bitstring.max_size):
            if self._in_set(i) and other_set._in_set(i):
                new_set._add_to_set(i)
        return new_set

    def difference(self, other_set: Self):
        """Elements that are in self but not in other_set."""
        new_set = Bitstring()
        for i in range(Bitstring.max_size):
            if self._in_set(i) and not other_set._in_set(i):
                new_set._add_to_set(i)
        return new_set

    def symmetric_difference(self, other_set: Self):
        """Elements that are in set A or set B, but not in both."""
        new_set = Bitstring()
        for i in range(Bitstring.max_size):
            if (self._in_set(i) or other_set._in_set(i)) and not (self._in_set(i) and other_set._in_set(i)):
                new_set._add_to_set(i)
        return new_set

def main():
    print("""CS 2130 - Encoding data with bits
This program takes two sets as input from the user and
shows the results of operations on the sets.""")

    a_size = int(input("How many elements in set A: "))
    set_a = Bitstring()
    set_a.get_input(a_size)

    b_size = int(input("How many elements in set B: "))
    set_b = Bitstring()
    set_b.get_input(b_size)

    print("")

    print("                          Set A:", set_a)
    print("                          Set B:", set_b)

    print("                Complement of A:", set_a.complement())
    print("                Complement of B:", set_b.complement())

    print("               Union of A and B:", set_a.union(set_b))
    print("        Intersection of A and B:", set_a.intersection(set_b))
    print("          Difference of A and B:", set_a.difference(set_b))
    print("Symmetric Difference of A and B:", set_a.symmetric_difference(set_b))



if __name__ == '__main__':
    main()
