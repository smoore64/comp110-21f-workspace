"""Counting letters in a string."""

__author__ = "730307980"

search: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
count: int = 0
while i < len(word):
    if word[i] == search:
        count = count + 1
    i = i + 1

print("Count: " + str(count))