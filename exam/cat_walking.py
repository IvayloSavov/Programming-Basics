minutes_walk = int(input())
number_walks_per_day = int(input())
calories_per_day = int(input())

burned_calories = minutes_walk * 5 * number_walks_per_day
percent_50_calories_ped_day = calories_per_day * 50/100

if burned_calories >= percent_50_calories_ped_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")