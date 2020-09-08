from sys import maxsize
from math import ceil
number_bake = int(input())
sugar = 0
flour = 0
max_sugar = -maxsize
max_flour = -maxsize
for bake in range (1, number_bake + 1):
    needed_sugar = int(input())
    sugar += needed_sugar
    needed_flour = int(input())
    flour += needed_flour
    if needed_sugar > max_sugar:
        max_sugar = needed_sugar
    if needed_flour > max_flour:
        max_flour = needed_flour
packets_sugar = ceil(sugar / 950)
packets_flour = ceil(flour / 750)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")