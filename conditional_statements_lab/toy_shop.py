# 1. Read input data
price_travel = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_lorry = int(input())
# 2. Prices of toys
price_puzzle = 2.60
price_dolls = 3
price_bears = 4.10
price_minions = 8.20
price_lorry = 2
# 3. Calculate the earned money
earned_money = number_puzzles * price_puzzle + number_bears * price_bears + number_dolls * price_dolls + number_minions * price_minions + number_lorry * price_lorry
# 4. Total toys
number_of_toys = number_lorry + number_minions + number_dolls + number_bears + number_puzzles
if number_of_toys >= 50:
    discount = 0.25
    earned_money = earned_money - earned_money * discount
# earned_money = earned_money * 0.75
rent = earned_money / 10
earned_money = earned_money - rent

difference = abs(earned_money - price_travel)
if earned_money >= price_travel:
    #ако тук няма равно ще гръмне, защото парите ще са ни достатъчни
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')