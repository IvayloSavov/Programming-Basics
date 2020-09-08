# 1. Read input data
price_travel = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
nummber_trucks = int(input())
# 2. Prices
price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2
# 3. Number_toys
number_toys = number_puzzles + number_dolls + number_bears + number_minions + nummber_trucks
# 4. Price toys
price_toys = (number_puzzles*price_puzzle) + (number_bears*price_bear) + (number_minions*price_minion) + (nummber_trucks*price_truck)
# 5. Check if the number of the toys is over 50
if number_toys >= 50:
    discount = price_toys * 0.25
    price_toys = price_toys - discount
# 6. Rent
rent = 0.10 * price_toys
money = price_toys - rent
# 7. Money left
money_left = abs(money - price_travel)
# 8. Check if the money are enough for the travel
if money >= price_travel:
    print(f"Yes! {money_left:.2f} lv left.")