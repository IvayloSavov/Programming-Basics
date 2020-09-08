from math import floor
from math import ceil
# 1. Read input data
price_rocket = float(input())
number_rockets = int(input())
number_trainers = int(input())
# 2. Price trainers
price_trainers = price_rocket * 1/6
# 3. total
total = (price_rocket * number_rockets) + (price_trainers*number_trainers)
# 4. Other equipment
other_equipment = total * 20/100
total = total + other_equipment
# 5. Money
money_djokovic = floor(total*1/8)
money_sponsors = ceil(total*7/8)
# 6. print
print(f"Price to be paid by Djokovic {money_djokovic}")
print(f"Price to be paid by sponsors {money_sponsors}")
