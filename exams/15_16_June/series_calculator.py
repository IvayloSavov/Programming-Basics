from math import floor
# 1. Read input data
name = input()
number_seasons = int(input())
number_episodes = int(input())
time_ordinary_episode = float(input())
# 2.
adds = time_ordinary_episode * 0.20
time_ordinary_episode += adds
extra_time_episode = number_seasons * 10
total_time = floor((time_ordinary_episode * number_episodes) * number_seasons + extra_time_episode)
# 3. Print
print(f"Total time needed to watch the {name} series is {total_time} minutes.")