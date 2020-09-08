budget = float(input())
number_nights = int(input())
price_one_night = float(input())
percent_more_expenses = int(input())/100

if number_nights > 7:
    price_one_night *= 0.95
total = (number_nights * price_one_night) + (percent_more_expenses * budget)

left_needed_money = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {left_needed_money:.2f} leva after vacation.")
else:
    print(f"{left_needed_money:.2f} leva needed.")