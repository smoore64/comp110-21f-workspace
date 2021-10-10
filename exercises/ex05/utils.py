"""List utility functions part 2."""

__author__ = "730307980"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Returns only evens in the list."""
    output: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            output.append(xs[i])
        i += 1
    return output


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a subset between the value of 2 indices."""
    output: list[int] = list()
    i: int = 0
    if start >= 0 and end < len(xs):
        i = start
        while i < end:
            output.append(xs[i])
            i += 1
    else:
        if start < 0 and end >= len(xs):
            output = xs
        else:
            if start < 0:
                start = 0
                i = 0
                while i < end:
                    output.append(xs[i])
                    i += 1
            else:
                if end >= len(xs):
                    end = len(xs)
                    i = start
                    while i < end:
                        output.append(xs[i])
                        i += 1
    return output


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """A function to combine 2 lists."""
    output: list[int] = list()
    output = xs + ys
    return output


    
        
    
    
