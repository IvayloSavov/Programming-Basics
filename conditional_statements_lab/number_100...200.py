num1 = int(input())

if num1 < 100:
    print('Less than 100')
elif num1 >= 100 and num1 <= 200:
    print('Between 100 and 200')
# 100 <= num1 <= 200: ТОВА Е ПО ПРАВИЛНОТО
elif num1 > 200:
    print('Greater than 200')