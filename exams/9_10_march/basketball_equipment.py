# 1. Read input data
basketball_fee = int(input())
# 2. Prices
price_trainers = basketball_fee - (basketball_fee*0.4)
price_team = price_trainers - (price_trainers*0.2)
price_ball = price_team * 1/4
price_accessories = price_ball * (1/5)
# Total
total = basketball_fee + price_trainers + price_team + price_ball + price_accessories
print(f'{total:.2f}')