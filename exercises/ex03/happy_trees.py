"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 1
depth: int = int(input("Depth: "))

if depth > 0:
    while i <= depth:
        print(TREE * i)
        i = i + 1