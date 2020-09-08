from math import ceil
# 1. Read input data
name = input()
duration_episode = int(input())
duration_brake = int(input())
# 2. Time - lunch, chill
time_lunch = duration_brake * 1/8
time_chill = duration_brake * 1/4
# 3. Left time
left_time = duration_brake - (time_lunch + time_chill)
# 4. Left needed time
left_needed_time = ceil(abs(left_time - duration_episode))
# 5. If
if left_time >= duration_episode:
    print(f"You have enough time to watch {name} and left with {left_needed_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {left_needed_time} more minutes.")