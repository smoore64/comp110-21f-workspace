"""Finding duplicate letters in a word."""

__author__ = "730307980"

i: int = 0
word: str = input("Enter a word: ")
dup: bool = False

while i < len(word):
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            dup = True
        else:
            dup = dup
        j = j + 1
    i = i + 1

print("Found duplicate: " + str(dup))
