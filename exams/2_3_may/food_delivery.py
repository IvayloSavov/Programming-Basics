# 1. Read input data
number_chicken = int(input())
number_fish = int(input())
number_vegan = int(input())
# 2. Prices
chicken = 10.35
fish = 12.40
vegan = 8.15
# 3. total
total_chicken = number_chicken * chicken
total_fish = number_fish * fish
total_vegan = vegan * number_vegan
# 4. Total
total = total_chicken + total_fish + total_vegan
# 5. desert
desert = total * 20/100
total = total + desert + 2.50
print(f"Total: {total:.2f}")