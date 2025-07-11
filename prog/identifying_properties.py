# Ty Davis
# 7/11/2025
# CS 2130
# Dr. Huson
# ---------
# Identifying Properties of a function
# filename: identifying_properties.py
from typing import List
type pair = tuple[int, int]

class Func:
    domain = [1, 2, 3, 4, 5]
    def __init__(self):
        self.pairs: List[pair] = []

    def get_input(self):
        """Ask user for how many pairs to provide, then retrieve the pairs"""
        while True:
            try:
                amount = int(input("Please enter the number of paired values as an integer: "))
                if amount < 0 or amount > len(Func.domain):
                    raise ValueError(f"The number must be 0-{len(Func.domain)}.")
                for i in range(amount):
                    my_pair = self._get_pair(i)
                    self._add_pair(my_pair)
                return
            except ValueError as e:
                print(e, "Please try again.")

    def _get_pair(self, i: int) -> pair:
        while True:
            try:
                pair_text = input(f"Please enter the ordered pair {i}: ")
                pair_vals = tuple([int(x) for x in pair_text.split()])
                if len(pair_vals) != 2:
                    raise ValueError(f"Please enter just 2")
                return pair_vals
            except ValueError as e:
                print(e, "Please try again.")

    def _add_pair(self, p: pair):
        self.pairs.append(p)

    def __str__(self) -> str:
        s: str = "The function is described by:\n"
        for x, y in self.pairs:
            s += f"F({x}) = {y}\n"
        return s

    @property
    def is_valid(self) -> bool:
        """No x value has two y values, and all x and y values are in the domain/range"""
        # check each x and y is in the domain
        for x, y in self.pairs:
            if x not in Func.domain or y not in Func.domain:
                return False

        # compare to see if any duplicates on the x-axis
        x_vals: List[int] = [p[0] for p in self.pairs]
        if len(set(x_vals)) != len(x_vals):
            return False
        return True

    @property
    def is_one_to_one(self) -> bool:
        """No y value has more than one x that maps to it"""

        # compare lengths to see if any duplicates on the y-axis
        y_vals: List[int] = [p[1] for p in self.pairs]
        if len(set(y_vals)) != len(y_vals):
            return False
        return True

    @property
    def is_onto(self) -> bool:
        """For every y in the Range, there is at least one x such that f(x)=y"""
        # Check that
        for y_val in Func.domain:
            if y_val not in [p[1] for p in self.pairs]:
                return False
        return self.is_valid

    @property
    def is_bijection(self) -> bool:
        """Function is both one-to-one and onto"""
        return self.is_one_to_one and self.is_onto

def main():
    # initialize and gather the function ordered-pairs
    a = Func()
    a.get_input()
    print(a)

    if a.is_valid:
        print("Is a valid function or partial function")
        # Only provide this feedback if it is valid
        print(f"Is {'NOT ' if not a.is_one_to_one else ''}one-to-one")
        print(f"Is {'NOT ' if not a.is_onto else ''}onto")
        print(f"Is {'NOT ' if not a.is_bijection else ''}a bijection")
    else:
        print("Is NOT a valid function or partial function")

if __name__ == '__main__':
    main()
