from math import floor
# 1. Read input data
record_in_seconds = float (input())
distance_in_meters = float (input())
time_swim_one_meter = float(input())
# 2. Time for swim
total_time_swim = distance_in_meters * time_swim_one_meter
# 3. Resistance
ressistance = floor(distance_in_meters / 15) * 12.5
# 4. Time for swim + resistance
time_swim = total_time_swim + ressistance

if time_swim < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_swim:.2f} seconds.")
else:
    not_enough_time = abs(record_in_seconds - time_swim)
    print(f'No, he failed! He was {not_enough_time:.2f} seconds slower.')
