# 1. Read input data
days_stayed = int(input())
room_type = input()
feedback = input()
price = 1
discount = 0
nights_stayed = days_stayed - 1
# 2. Check room type
if room_type == "apartment":
    price = 25
# 2.1 Check nights staying -> discount
    if nights_stayed < 10:
        discount = 0.3
    elif 10 <= nights_stayed <= 15:
        discount = 0.35
    elif nights_stayed > 15:
        discount = 0.5
elif room_type == "president apartment":
    price = 35
elif room_type == "room for one person":
    price = 18
# 3. Calculate price with discount
total_price = nights_stayed * price
total_price = total_price * (1 - discount)
# 4. Check feedback
if feedback == "positive":
# 4.1. + -> 25% +
    total_price += total_price * 0.25
else:
# total price * 0.9
# 4.2 - -> -10%
total_price -= total_price * 0.1
# 5. Print
print(total_price)