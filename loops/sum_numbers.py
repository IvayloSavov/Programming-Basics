# 1. read input data
numbers_count = int(input())
sum_numbers = 0

for number in range(numbers_count):
    current_number = int(input())
    sum_numbers += current_number

print(sum_numbers)