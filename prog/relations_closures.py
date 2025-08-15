# Ty Davis
# Relations: Properties and Closures
# CS2130 - Dr. Huson
# 8/15/2025

import re
import copy

def collect_matrix():
    msg = """You may have up to a 20x20 matrix, entered as a set of
ordered pairs one ordered pair per line. For example, 1 3
results in a 1 in row 1, column 3. Please enter the matrix
as ordered pairs x y (0 0 to end matrix input)"""
    print(msg)
    pairs = []
    # get the input from the user
    while True:
        s = input("")
        obj = re.match(r'(\d+)\s+(\d+)', s)
        
        if not obj:
            print("There was an error in your input, try again.")
            continue

        i = int(obj.group(1))
        j = int(obj.group(2))
        if i > 20 or j > 20:
            print("Maximum size is 20 x 20 array, try again.")
            continue

        # break if 0, 0
        if i == 0 and j == 0:
            break

        pairs.append((i, j))

    m = max([max(pair[0], pair[1]) for pair in pairs])

    # build the matrix now
    a = [[0 for _ in range(m)] for _ in range(m)]
    for i, j in pairs:
        a[i-1][j-1] = 1

    return a

def print_matrix(a, msg=""):
    # print a message if there is one
    if msg:
        print(msg)

    # print the matrix
    for row in a:
        for j in row:
            print(j, end=" ")
        print()
    print()

def meet(a, b, m):
    c = [[0 for _ in range(m)] for _ in range(m)]

    # boolean AND
    for i in range(m):
        for j in range(m):
            if a[i][j] and b[i][j]:
                c[i][j] = 1
    return c

def join(a, b, m):
    c = [[0 for _ in range(m)] for _ in range(m)]
    
    # boolean OR
    for i in range(m):
        for j in range(m):
            if a[i][j] or b[i][j]:
                c[i][j] = 1
    return c

def boolean_product(a, b, m):
    c = [[0 for _ in range(m)] for _ in range(m)]

    # boolean product of A and B
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j] = c[i][j] or a[i][k] and b[k][j]
    return c

def complement(a, m):
    c = [[0 for _ in range(m)] for _ in range(m)]
    
    # boolean NOT
    for i in range(m):
        for j in range(m):
            c[i][j] = 0 if a[i][j] else 1
    return c

def transpose(a, m):
    c = [[0 for _ in range(m)] for _ in range(m)]

    # reflect over diagonal
    for i in range(m):
        for j in range(m):
            c[j][i] = a[i][j]
    return c

def is_reflexive(a, m):
    # is the diagonal all 1?
    for i in range(m):
        if not a[i][i]:
            return False
    return True

def is_symmetric(a, m):
    # is it symmetric across the diagonal?
    for i in range(m):
        for j in range(m):
            if a[i][j] != a[j][i]:
                return False
    return True

def is_antisymmetric(a, m):
    # is there no symmetry at all across the diagonal?
    for i in range(m):
        for j in range(m):
            if i != j and (a[i][j] == 1 and a[j][i] == 1):
                return False
    return True

def is_transitive(a, m):
    # do all the right triangles exist?
    for i in range(m):
        for j in range(m):
            if a[i][j]:
                for k in range(m):
                    if a[j][k] and not a[i][k]:
                        return False
    return True

def reflexive_closure(a, m):
    # return copy of a but ensure that it is reflexive
    c = copy.deepcopy(a)
    for i in range(m):
        c[i][i] = 1
    return c

def symmetric_closure(a, m):
    # return a copy of a but ensure it is symmetric
    c = copy.deepcopy(a)
    for i in range(m):
        for j in range(m):
            if c[i][j]:
                c[j][i] = 1
    return c

def transitive_closure(a, m):
    # return a copy of a but ensure it is transitive
    w = copy.deepcopy(a)
    for k in range(m):
        for i in range(m):
            for j in range(m):
                w[i][j] = w[i][j] or (w[i][k] and w[k][j])
    return w

def expand_matrix(a, m, new_m):
    # expand a to new_m x new_m matrix with zeros
    c = [[0 for _ in range(new_m)] for _ in range(new_m)]
    for i in range(m):
        for j in range(m):
            c[i][j] = a[i][j]
    return c


def main():
    # collect the matrices
    a = collect_matrix()
    print_matrix(a, "Array A =")
    b = collect_matrix()
    print_matrix(b, "Array B =")

    # make sure that a and b are the same size
    m_a = len(a)
    m_b = len(b)
    m = m_a
    if m_a > m_b:
        m = m_a
        b = expand_matrix(b, m_b, m_a)
    elif m_a < m_b:
        m = m_b
        a = expand_matrix(a, m_a, m_b)

    # display information about the matrices
    print_matrix(meet(a, b, m), "The meet of A and B:")
    print_matrix(join(a, b, m), "The join of A and B:")
    print_matrix(boolean_product(a, b, m), "The boolean product of A and B:")
    print_matrix(complement(a, m), "The complement of A:")
    print_matrix(transpose(a, m), "The transpose of A:")

    print(f"Relation A is{' NOT' if not is_reflexive(a, m) else ''} reflexive.")
    print(f"Relation A is{' NOT' if not is_symmetric(a, m) else ''} symmetric.")
    print(f"Relation A is{' NOT' if not is_antisymmetric(a, m) else ''} antisymmetric.")
    print(f"Relation A is{' NOT' if not is_transitive(a, m) else ''} transitive.")

    print_matrix(reflexive_closure(a, m), "The reflexive closure of A:")
    print_matrix(symmetric_closure(a, m), "The symmetric closure of A:")
    print_matrix(transitive_closure(a, m), "The transitive closure of A:")


if __name__ == '__main__':
    main()
