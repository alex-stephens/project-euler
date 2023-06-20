# Project Euler
# Problem 64

# Odd period square roots

def get_perfect_squares(max_val):
    squares = []
    n = 1
    while n**2 <= max_val:
        squares.append(n**2)
        n += 1
    return squares

def get_continued_fraction(n):
    """Returns the continued fraction representation of s, as a single and repeating component."""

    vals = []

    s = int(n**0.5)
    vals.append(s)

    # Construct expressions of the form a + (sqrt(n) - x) / y
    a = s
    x = s
    y = 1

    terms = {}
    i = 1
    repeat_start = None

    while True:
        y = (n - x**2) / y
        a = int((s + x) / y)
        x = a * y - x

        if i > 1 and (a, x, y) in terms:
            repeat_start = terms[(a, x, y)]
            break

        terms[(a, x, y)] = i
        vals.append(a)
        i += 1

    return vals[0:repeat_start], vals[repeat_start:]

def main():

    MAX_VAL = 10000
    squares = set(get_perfect_squares(MAX_VAL))
    count = 0

    for n in range(2, MAX_VAL + 1):
        if n in squares:
            continue

        _, repeating = get_continued_fraction(n)
        if len(repeating) % 2 == 1:
            count += 1

    print(count)


if __name__ == "__main__":
    main()