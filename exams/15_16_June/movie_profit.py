# 1. Read input data
name_film = input()
days = int(input())
tickets = int(input())
price_ticket = float(input())
percent_for_cinema = int(input()) / 100
# 2. Money
money = tickets * price_ticket * days
# 3. Percent
percent_for_cinema = money * percent_for_cinema
money -= percent_for_cinema
# 4. Print
print(f"The profit from the movie {name_film} is {money:.2f} lv.")
