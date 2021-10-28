"""Practice with dictionaries."""

__author__ = "730307980"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary."""
    output = {}
    for key in a:
        if a[key] in output:
            raise KeyError("Duplicate keys in new list.")
        else:
            output[a[key]] = key
    return output


def favorite_color(a: dict[str, str]) -> str:
    """Returns favorite Color."""
    output: str
    favorite = {}
    for key, value in a.items():
        if value not in favorite:
            favorite[value] = 0
        else:
            favorite[value] += 1
    output = str(max(favorite, key=favorite.get))
    return output


def count(a: list[str]) -> dict[str, int]:
    """Returns count of items in a list."""
    output: dict[str, int] = {}
    i: int = 0
    while i < len(a):
        for y in a:
            if y in output:
                if a[i] == y:
                    output[y] += 1
            else:
                output[y] = 1
            i += 1
    return output