# 1. Read input data
profit_needed = float(input())
command = input()
current_profit = 0
order = 0
while command != "Party!" and current_profit < profit_needed:
    name_cocktail = str(command)
    number_cocktails = int(input())
    price_cocktail = len(name_cocktail)
    order += 1
    order_profit = number_cocktails * price_cocktail
    if not order_profit % 2 == 0:
        order_profit *= 75/100
    current_profit += order_profit
    if current_profit >= profit_needed:
        break
    else:
        command = input()

if command == "Party!":
    if current_profit < profit_needed:
        need_money = profit_needed - current_profit
        print(f"We need {need_money:.2f} leva more.")
    else:
        print("Target acquired.")

if current_profit >= profit_needed:
    print("Target acquired.")

print(f"Club income - {current_profit:.2f} leva.")

