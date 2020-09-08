from math import floor
record = float(input())
distances = float(input())
time_for_1_meter = float(input())

drag = floor(distances/50) * 30
total_time = (distances * time_for_1_meter) + drag

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")