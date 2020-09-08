import sys
# 1. Read input data
count_numbers = int(input())

biggest_number = -sys.maxsize
smallest_number = sys.maxsize
for position in range(count_numbers):
    current_number = int(input())
    if current_number > biggest_number:
        biggest_number = current_number
    if current_number < smallest_number:
        smallest_number = current_number

print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')
