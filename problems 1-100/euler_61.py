# Project Euler
# Problem 62

# Cyclical figurate numbers

import math
import logging


def main():
    N_min, N_max = 3, 8
    N_vals = list(range(N_min, N_max + 1))
    min_val, max_val = 1000, 9999

    polygonals = {N: generate_polygonal_in_range(N, min_val, max_val) for N in N_vals}
    cycle = find_cycle(polygonals)

    print(f"{cycle = }")
    print(sum((x[0] for x in cycle)))


def is_pair(n1, n2):
    if n1 is None:
        return True
    return str(n1[0])[2:] == str(n2[0])[:2]


def get_successors(x, orders, polygonals):
    succ = []
    for o in orders:
        for y in polygonals[o]:
            if is_pair(x, (y, o)):
                succ.append((y, o))
    return list(succ)


def dfs(current_path, orders, polygonals):
    x = None if len(current_path) == 0 else current_path[-1]

    # If there are no more orders to check,
    # check that the path is a cycle
    if len(orders) == 0:
        if is_pair(current_path[-1], current_path[0]):
            return list(current_path)
        else:
            return []

    succ = get_successors(x, orders, polygonals)

    for s in succ:
        new_path = list(current_path)
        new_path.append(s)

        new_orders = set(orders)
        new_orders.remove(s[1])

        extended_path = dfs(new_path, new_orders, polygonals)
        if len(extended_path) == 0:
            continue
        return extended_path

    return []


def find_cycle(polygonals):
    orders = set(polygonals.keys())
    current_path = ()
    solution = dfs(current_path, orders, polygonals)
    return solution


def generate_polygonal(N, n):

    if N == 3:
        return n * (n + 1) // 2
    elif N == 4:
        return n**2
    elif N == 5:
        return n * (3 * n - 1) // 2
    elif N == 6:
        return n * (2 * n - 1)
    elif N == 7:
        return n * (5 * n - 3) // 2
    elif N == 8:
        return n * (3 * n - 2)
    else:
        logging.error(f"Invalid N : {N}")
        return 0


def generate_polygonal_in_range(N, min_value=0, max_value=1):
    result = []
    for n in range(int(math.sqrt(2 * (max_value + 1)))):
        x = generate_polygonal(N, n)
        if x > max_value:
            break
        if x >= min_value:
            result.append(x)
    return set(result)


if __name__ == "__main__":
    main()
