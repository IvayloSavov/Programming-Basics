# 1. Read input data
budget = int(input())
season = input()
number_fisherman = int(input())
price_ship = 0
# 2. Price ship
if season == "Spring":
    price_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_ship = 4200
elif season == "Winter":
    price_ship = 2600
# 3. Discount ship:
if number_fisherman <= 6:
    # price *= 0.9
    discount = price_ship * 10/100
    price_ship = price_ship - discount
elif 7 <= number_fisherman <= 11:
    # price *= 0.85
    discount = price_ship * 15/100
    price_ship = price_ship - discount
elif number_fisherman > 12:
    # price = 0.75
    discount = price_ship * 25/100
    price_ship = price_ship - discount
# 4. Bonus discount:
if number_fisherman % 2 == 0 and season != "Autumn":
    # price *= 0.95
    bonus_discount = price_ship * 5/100
    price_ship = price_ship - bonus_discount
# 5. Check budget:
money_left_needed = abs(budget - price_ship)
if budget >= price_ship:
    print(f"Yes! You have {money_left_needed:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left_needed:.2f} leva.")