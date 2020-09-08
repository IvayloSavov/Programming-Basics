budget = int(input())
price_towel = float(input())
percent_discount = int(input())

price_umbrella = price_towel * 2/3
price_flip_flops = price_umbrella * 75/100
price_beach_bag = (price_flip_flops + price_towel) * 1/3

total_money_spend = price_towel + price_umbrella + price_flip_flops + price_beach_bag
discount = total_money_spend * percent_discount/100
total_money_spend -= discount

if budget >= total_money_spend:
    print(f"Annie's sum is {total_money_spend:.2f} lv. She has {budget - total_money_spend:.2f} lv. left.")
else:
    print(f"Annie's sum is {total_money_spend:.2f} lv. She needs {total_money_spend - budget:.2f} lv. more.")