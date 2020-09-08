from math import floor
# 1. Read input data
hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())
# 2. All time exam
all_time_exam = (hour_exam * 60) + minutes_exam
# 3. All time arrive
all_time_arrive = (hour_arrive * 60) + minutes_arrive
# 4. Check
difference = abs(all_time_arrive - all_time_exam)
if all_time_exam < all_time_arrive:
    print("Late")
    if difference > 59:
        hours = floor(difference / 60)
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    else:
        print(f'{difference} minutes after the start')
elif all_time_exam == all_time_arrive:
    print("On time")
elif difference <= 30:
    print("On time")
    if difference > 59:
        hours = floor(difference / 60)
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
    else:
        print(f'{difference} minutes before the start')
elif all_time_exam > all_time_arrive and difference > 30:
    print("Early")
    if difference > 59:
        hours = floor(difference / 60)
        minutes = difference % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
    else:
        print(f'{difference} minutes before the start')
