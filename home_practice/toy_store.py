# 1. Prices of toys
price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2
# 2. Read input data
price_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
# 3. Number of toys
number_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
# 4. Money of toys
money_toys = number_puzzles * price_puzzle + number_dolls * price_doll + number_bears * price_bear + number_trucks * price_truck + number_minions * price_minion
# 5. Discount
if number_toys >= 50:
    discount = money_toys * 0.25
    money_toys = money_toys - discount
# 6. Rent for the shop
rent = money_toys * 0.1
money_toys = money_toys - rent
enough_money = abs(money_toys - price_trip)

if money_toys >= price_trip:
    print(f'Yes! {enough_money:.2f} lv left.')
else:
    print(f'Not enough money! {enough_money:.2f} lv needed')

