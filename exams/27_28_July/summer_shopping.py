# 1. Read input data
budget = int(input())
price_towel = float(input())
discount_percent = (int(input())/100)
# 2. Prices
price_umbrella = price_towel * (2/3)
price_flip_flops = price_umbrella * 0.75
price_bag = (price_flip_flops + price_towel) * (1/3)
# 3. Total price
total_price = price_towel + price_umbrella + price_flip_flops + price_bag
# 4. Discount
discount = total_price * discount_percent
total_price = total_price - discount
money_left = abs(budget-total_price)
# 5. Check if the budget is enough
if budget >= total_price:
    print(f"Annie's sum is {total_price:.2f} lv. She has {money_left:.2f} lv. left.")
else:
    print(f"Annie's sum is {total_price:.2f} lv. She needs {money_left:.2f} lv. more.")