budget = float(input())
number_statist = int(input())
price_outfit_one_statist = float(input())

decor = budget * 10/100

if number_statist > 150:
    money_clothes = price_outfit_one_statist * number_statist * 90/100
    total_needed_money = decor + money_clothes
else:
    total_needed_money = decor + number_statist * price_outfit_one_statist

needed_left_money = abs(total_needed_money - budget)

if budget >= total_needed_money:
    print("Action!")
    print(f"Wingard starts filming with {needed_left_money:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {needed_left_money:.2f} leva more.")
