# 1. Read input data
film = input()
packet_film = input()
number_tickets = int(input())
price = 0
# 2. Price
if film == "John Wick":
    if packet_film == "Drink":
        price = 12
    elif packet_film == "Popcorn":
        price = 15
    elif packet_film == "Menu":
        price = 19
elif film == "Star Wars":
    if packet_film == "Drink":
        price = 18
    elif packet_film == "Popcorn":
        price = 25
    elif packet_film == "Menu":
        price = 30
elif film == "Jumanji":
    if packet_film == "Drink":
        price = 9
    elif packet_film == "Popcorn":
        price = 11
    elif packet_film == "Menu":
        price = 14
# 3. total
total = price * number_tickets
# 4. Discount
if film == "Star Wars" and number_tickets >= 4:
    total = total * 0.70
elif film == "Jumanji" and number_tickets == 2:
    total = total * 0.85
# 5. Print
print(f"Your bill is {total:.2f} leva.")

