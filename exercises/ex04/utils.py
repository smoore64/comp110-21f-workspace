"""List utility functions."""

__author__ = "730307980"


# all function


def all(b: list[int], a: int) -> bool:
    """Checking if an int is equal to a list."""
    i: int = 0
    while i < len(b):
        if b[i] == a:
            if i == len(b) - 1:
                return True
            i += 1
        else:
            return False
    return False


# is_equal function


def is_equal(a: list[int], b: list[int]) -> bool:
    """Checking if a list is equal to a list."""
    i = 0 
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a) == 0 and len(b) > 0:
        return False
    if len(a) > 0 and len(b) == 0:
        return False

    while i < len(a) and i < len(b):
        if a[i] == b[i]:
            if i == len(a) - 1 and i == len(b) - 1:
                if len(a) == len(b):
                    if a[len(a) - 1] == b[len(b) - 1]:
                        return True
            i += 1
        else:
            return False
    return False


# max secion


def max(input: list[int]) -> int:
    """Checking what the max value of a list is."""
    i = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    else:
        while i < len(input):
            j = i + 1
            while j < len(input):
                if input[i] > input[j]:
                    if j == len(input) - 1:
                        if input[i] >= input[len(input) - 1]:
                            return input[i]
                    j += 1
                else:
                    j += len(input)
            i += 1
    return input[len(input) - 1]