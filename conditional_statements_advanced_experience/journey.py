# 1. Read input data
budget = float(input())
season = input()
# 2. If
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money = budget * 30/100
        type_of_holiday = "Camp"
    elif season == "winter":
        money = budget * 70/100
        type_of_holiday = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money = budget * 40 / 100
        type_of_holiday = "Camp"
    elif season == "winter":
        money = budget * 80 / 100
        type_of_holiday = "Hotel"
elif budget > 1000:
    destination = "Europe"
    money = budget * 90/100
    type_of_holiday = "Hotel"
# 3. Print
print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {money:.2f}')
