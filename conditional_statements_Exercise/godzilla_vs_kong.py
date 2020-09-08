# 1. Read input data
budget_fiml = float(input())
number_statist = int(input())
price_clothes_one_statist = float(input())
# 2. Decor
decor = budget_fiml * 0.1

if number_statist > 150:
    discount_clothes = price_clothes_one_statist * 0.1
    price_clothes_one_statist = price_clothes_one_statist - discount_clothes
    price_clothes = number_statist * price_clothes_one_statist
else:
    price_clothes = number_statist * price_clothes_one_statist

total_price = price_clothes + decor

#може и тук да сложа едно общо вместо две във всеки if. Говоря за not_enough_money и enough_money

if total_price > budget_fiml:
    print("Not enough money!")
    not_enough_money = abs(total_price - budget_fiml)
    print(f'Wingard needs {not_enough_money:.2f} leva more.')
elif total_price <= budget_fiml:
    print("Action!")
    enough_money = abs(total_price - budget_fiml)
    print(f"Wingard starts filming with {enough_money:.2f} leva left.")