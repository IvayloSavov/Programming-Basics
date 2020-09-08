# 1. Read input data
town = input()
sales = float(input())
is_valid = True

if town == "Sofia":
    if 0 <= sales <= 500:
        comission = 5/100
    elif 500 < sales <= 1000:
        comission = 7/100
    elif 1000 < sales <= 10000:
        comission = 8/100
    elif sales > 10000:
        comission = 12/100
    else:
        is_valid = False
        print('error')
elif town == "Varna":
    if 0 <= sales <= 500:
        comission = 4.5 / 100
    elif 500 < sales <= 1000:
        comission = 7.5 / 100
    elif 1000 < sales <= 10000:
        comission = 10 / 100
    elif sales > 10000:
        comission = 13 / 100
    else:
        is_valid = False
        print('error')
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        comission = 5.5/100
    elif 500 < sales <= 1000:
        comission = 8/100
    elif 1000 < sales <= 10000:
        comission = 12/100
    elif sales > 10000:
        comission = 14.5/100
    else:
        is_valid = False
        print('error')
else:
    is_valid = False
    print('error')

if is_valid:
    money = sales * comission
    print(f'{money:.2f}')