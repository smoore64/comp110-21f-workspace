"""List utility functions."""

__author__ = "730307980"


# all function


def all(a: list[int], b: int) -> bool:
    i: int = 0
    while i < len(a):
        if a[i] == b:
            i += 1
        else:
            return False
    return True


# is_equal function


def is_equal(a: list[int], b: list[int]) -> bool:
    i = 0 
    while i < len(a) or i < len(b):
        if a[i] == b[i]:
            i += 1
        else:
            return False
    return True


# max secion


def max(input: list[int]) -> int:
    big: int = max(input)
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        print(big)
    return big