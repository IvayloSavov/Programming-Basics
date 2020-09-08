# 1. Read input data
budget_film = float(input())
destination = input()
season = input()
number_days = int(input())
price = 0
# 2. prices
if season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250
elif season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
# 3. tax reliefs
total = price * number_days
if destination == "Dubai":
    total *= 0.70
elif destination == "Sofia":
    taxes = total * 0.25
    total += taxes
# 5. If budget is enough
left_needed_money = abs(total - budget_film)
if budget_film >= total:
    print(f"The budget for the movie is enough! We have {left_needed_money:.2f} leva left!")
else:
    print(f"The director needs {left_needed_money:.2f} leva more!")