# Project Euler
# Problem 206

# Concealed square

from math import isqrt


def is_match(n):
    target = "1_2_3_4_5_6_7_8_9_0"
    s = str(n)

    if len(s) != len(target):
        return False

    for i, c in enumerate(target):
        if c == "_":
            continue
        if c != s[i]:
            return False
    return True


def main():
    target_min = isqrt(1020304050607080900)
    target_max = isqrt(1929394959697989990)

    n = (target_min // 10) * 10

    while n < target_max:
        if is_match(n**2):
            break
        n += 10

    print(n)


if __name__ == "__main__":
    main()
