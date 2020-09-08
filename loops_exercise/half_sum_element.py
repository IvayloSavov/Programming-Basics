import sys
# 1. Read input data
n = int(input())

biggest_number = -sys.maxsize
score = 0

for num in range(n):
    number = int(input())
    if number > biggest_number:
        biggest_number = number

    score += number
score -= biggest_number
if score == biggest_number:
    print("Yes")
    print(f"Sum = {score}")
else:
    print("No")
    print(f"Diff = {abs(score - biggest_number)}")