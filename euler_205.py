# Project Euler
# Problem 204

# Dice Game

from itertools import product


def main():

    # (num dice, sides) per player
    p1 = (9, 4)
    p2 = (6, 6)

    d1, d2 = compute_dist(*p1), compute_dist(*p2)
    p = compute_win_prob(d1, d2)
    print(f"{p:.7f}")


def compute_win_prob(d1, d2):
    """
    Computes the win probability for player 1.
    """

    result = 0

    for v1 in d1:
        for v2 in d2:
            if v1 <= v2:
                continue
            result += d1[v1] * d2[v2]
    return result


def compute_dist(num_dice, sides):
    """
    Computes probabilities of each outcome for the player.
    """
    result = {}
    inc_p = 1 / (sides**num_dice)

    for r in product(range(1, sides + 1), repeat=num_dice):

        v = sum(r)
        if v not in result:
            result[v] = 0
        result[v] += inc_p

    return result


if __name__ == "__main__":
    main()
