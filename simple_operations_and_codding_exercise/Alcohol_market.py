# 1.Read input data
price_whiskey = float(input())
number_beers = float(input())
number_wine = float(input())
number_rakia = float(input())
number_whiskey = float(input())
# 2. Discounts for the alcohol
price_rakia = price_whiskey / 2
discount_wine = price_rakia * 0.4
discount_beer = price_rakia * 0.8
# 3. Prices for the alcohols
price_wine = price_rakia - discount_wine
price_beer = price_rakia - discount_beer
# 4. Sum for the alcohols
rakia = price_rakia * number_rakia
beer = price_beer * number_beers
whiskey = price_whiskey * number_whiskey
wine = price_wine * number_wine
# 5. Need money
need_money = rakia + beer + whiskey + wine
# 6. Print
print(f'{need_money:.2f}')

