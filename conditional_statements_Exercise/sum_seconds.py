from math import floor
# 1. Read input data
time_first = int(input())
time_second = int(input())
time_third = int(input())
# 2. Total time
total_time = time_first + time_second + time_third
# 3. Minutes and seconds
minutes = total_time / 60
seconds = total_time % 60 #така намираме секундите като разделим на 60 намираме минутите, а остатъкът е секунидте които са последните всъщност
#тотал тайма се дели на 60 и така намираме минутите, а остатъкът се явяват секундите

minutes = floor(minutes)

# 4.Printing results
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    (print(f'{minutes}:{seconds}'))