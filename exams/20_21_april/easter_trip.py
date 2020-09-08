# 1. Read input data
destination = input()
dates_reservation = (input())
number_nights = int(input())
price = 1
if destination == "France":
    if dates_reservation == "21-23":
        price = 30
    elif dates_reservation == "24-27":
        price = 35
    elif dates_reservation == "28-31":
        price = 40
elif destination == "Italy":
    if dates_reservation == "21-23":
        price = 28
    elif dates_reservation == "24-27":
        price = 32
    elif dates_reservation == "28-31":
        price = 39
elif destination == "Germany":
    if dates_reservation == "21-23":
        price = 32
    elif dates_reservation == "24-27":
        price = 37
    elif dates_reservation == "28-31":
        price = 43

expenses = number_nights * price
print(f"Easter trip to {destination} : {expenses:.2f} leva.")