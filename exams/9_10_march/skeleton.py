# 1. Read input data
minutes_to_beat = int(input())
seconds_to_beat = int(input())
long_canal = float(input())
seconds_for_100_meters = int(input())
seconds_for_1_meter = seconds_for_100_meters / 100
# 2. Convert
seconds_to_beat = seconds_to_beat + (minutes_to_beat*60)
# 3. Drag
drag = long_canal/120 * 2.5
# 4. Time
time_martin = long_canal * seconds_for_1_meter - drag
# 5. Check if
if time_martin <= seconds_to_beat:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_martin:.3f}.")
else:
    needed_seconds = (time_martin - seconds_to_beat)
    print(f"No, Marin failed! He was {needed_seconds:.3f} second slower.")