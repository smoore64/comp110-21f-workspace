"""Repeating a beat in a loop."""

__author__ = "730307980"


beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
output: str = (beat + " ")
    
if number > 0:
    while i < number:
        if i < number - 1:
            print(beat + " ", end="")
        else:
            print(beat)
        i = i + 1

else:
    print("No beat...")
