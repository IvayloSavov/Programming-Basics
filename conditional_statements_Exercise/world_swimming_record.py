from math import floor
# 1. Read input data
record = float(input())
distance = float(input())
time = float(input())

# 2. Total time
total_time = distance * time

delay = floor(distance / 15) * 12.5
total_time += delay
print(delay)
if total_time < record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    differencce = total_time - record
    print(f'No, he failed! He was {differencce:.2f} seconds slower.')