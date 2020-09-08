# 1. Read input data
type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 1
price_total = 0
# 2. If type of flower
if type_flowers == "Roses":
    price = 5
elif type_flowers == "Dahlias":
    price = 3.80
elif type_flowers == "Tulips":
    price = 2.80
elif type_flowers == "Narcissus":
    price = 3
elif type_flowers == "Gladiolus":
    price = 2.50
price_total = number_flowers * price
# 3. Discount
if type_flowers == "Roses" and number_flowers > 80:
    discount = price_total * 10/100
    price_total = price_total - discount
elif type_flowers == "Dahlias" and number_flowers > 90:
    discount = price_total * 15 / 100
    price_total = price_total - discount
elif type_flowers == "Tulips" and number_flowers > 80:
    discount = price_total * 15 / 100
    price_total = price_total - discount
elif type_flowers == "Narcissus" and number_flowers < 120:
    raise_the_cost = price_total * 15 / 100
    price_total = price_total + raise_the_cost
elif type_flowers == "Gladiolus" and number_flowers < 80:
    raise_the_cost = price_total * 20 / 100
    price_total = price_total + raise_the_cost
money = abs(budget - price_total)
if budget >= price_total:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {money:.2f} leva more.")
