"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730307980"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
fortune: int = randint(1, 4)

if fortune == 1:
    print("The fortune you seek is in another program.")
else:
    if fortune == 2:
        print("You will die alone and poorly dressed.")
    else:
        if fortune == 3:
            print("He who laughs at himself never runs out of things to laugh at.")
        else:
            if fortune == 4:
                print("The road to riches is paved with homework.")


print("Now, go spread positive vibes!")
