# 1. Read input data
budget = float(input())
number_fuel = float(input())
day_week = input()
# 2. Money
price_fuel = 2.10
price_ekskurzovod = 100
money_fuel = number_fuel * price_fuel
# 3. Total
total = price_ekskurzovod + money_fuel
# 4. If day
if day_week == "Saturday":
    discount = total * 10/100
    total = total - discount
elif day_week == "Sunday":
    discount = total * 20 / 100
    total = total - discount
# 5. Money_left_needed
money_left_needed = abs(budget - total)
# 5. If budget
if budget >= total:
    print(f"Safari time! Money left: {money_left_needed:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {money_left_needed:.2f} lv.")
