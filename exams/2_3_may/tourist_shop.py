# 1. Read input data
budget = float(input())

# 2. Variable
number_products = 0
total_money = 0
for product in range(1, 100000000):
    name_product = input()
    if name_product != "Stop":
        price_product = float(input())
        if product % 3 == 0:
            price_product /= 2
            number_products += 1
            total_money += price_product
            budget -= price_product
        elif price_product > budget:
            break
        else:
            number_products += 1
            total_money += price_product
            budget -= price_product
    if name_product == "Stop":
        break

if name_product == "Stop":
    print(f"You bought {number_products} products for {total_money:.2f} leva.")
elif price_product > budget:
    needed_money = price_product - budget
    print(f"You don't have enough money!\nYou need {needed_money:.2f} leva!")