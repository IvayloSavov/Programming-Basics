# 1. Read input data
time_photos = int(input())
number_scenes = int(input())
time_one_scene = int(input())
# 2. Arrangement time
arrangement_time = time_photos * 0.15
time_photos -= arrangement_time
# 3. Total time
total_time = number_scenes * time_one_scene
# 4.
time_left_needed = round(abs(total_time-time_photos))
if time_photos >= total_time:
    print(f"You managed to finish the movie on time! You have {time_left_needed} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {time_left_needed} minutes.")
