from sys import maxsize

budget = float(input())
is_stop = False
too_expensive = False
count_products = 0
total_spend = 0
product = 0
for product in range(1, maxsize):
    product_type = input()
    if product_type == "Stop":
        is_stop = True
        break
    price = float(input())
    if product % 3 == 0:
        price /= 2
        if price > budget:
            too_expensive = True
            break
    if price > budget:
        too_expensive = True
        break
    else:
        count_products += 1
        budget -= price
        total_spend += price

if is_stop:
    print(f"You bought {count_products} products for {total_spend:.2f} leva.")
if too_expensive:
    needed_money = price - budget
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")