days_vacation = int(input())
left_money = 0
for day in range(1, days_vacation+1):
    max_money = 60
    count_products = 0
    if left_money > 0:
        max_money += left_money
    while max_money > 0:
        price_product = input()
        if price_product == "Day over":
            if max_money > 0:
                print(f"Money left from today: {max_money:.2f}. You've bought {count_products} products.")
            break
        else:
            price_product = float(price_product)
            if max_money < price_product:
                pass
            else:
                max_money -= price_product
                count_products += 1
                if max_money == 0:
                    print(f"Daily limit exceeded! You've bought {count_products} products.")

    if max_money > 0:
        left_money = max_money
