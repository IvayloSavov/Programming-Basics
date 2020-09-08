from math import floor
# 1. Read input data
kg_lemons = float(input())
kg_sugar = float(input())
l_water = float(input())
# 2. Lemonade
lemonade = kg_lemons * 980
lemonade = lemonade + (l_water * 1000) + (0.3 * kg_sugar)
# 3. Cups
cups = floor(lemonade / 150)
# 4. Profit
profit = cups * 1.20
# 5. Print
print(f'All cups sold: {cups}')
print(f'Money earned: {profit:.2f}')