from math import ceil, floor
record_seconds = float(input())
distance_metres = float(input())
time_for_1_meter = float(input())

incline_hard = floor(distance_metres / 50) * 30
time_georgi = time_for_1_meter * distance_metres
time_georgi_plus_incline = time_georgi + incline_hard

time = abs(time_georgi_plus_incline - record_seconds)
if time_georgi_plus_incline >= record_seconds:
    print(f"No! He was {time:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {time_georgi_plus_incline:.2f} seconds.")