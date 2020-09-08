# 1. Read input data
max_power = int(input())

for power in range (0, max_power + 1, 2):
    number = 2 ** power
    print(number)