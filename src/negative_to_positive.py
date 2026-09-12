#!/usr/bin/env python3


def negative_to_positive(n: int) -> list:
    """
    Given a positive integer n, return a list of every integer from -n to n,
    in ascending order, skipping 0.

    For example:
        negative_to_positive(2)   # -> [-2, -1, 1, 2]
        negative_to_positive(3)   # -> [-3, -2, -1, 1, 2, 3]

    Practice using range() together with a condition that filters out 0.
    """
    # TODO: implement using range(-n, n + 1) and skip the value 0
    pass


def main():
    n = int(input("Please type in a number: "))
    for value in negative_to_positive(n):
        print(value)


if __name__ == "__main__":
    main()
