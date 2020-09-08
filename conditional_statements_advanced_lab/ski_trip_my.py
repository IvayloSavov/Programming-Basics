# 1. Read input data
days_stay = int(input())
type_room = input()
feedback = input()
discount = True
days_stay = days_stay - 1
# 2. Prices
if type_room == "room for one person":
    price = 18
    if days_stay < 10:
        discount = False
    elif 10 <= days_stay <= 15:
        discount = False
    elif days_stay > 15:
        discount = False
elif type_room == "apartment":
    price = 25
    if days_stay < 10:
        discount = price * 30/100 * days_stay
    elif 10 <= days_stay <= 15:
        discount = price * 35/100 * days_stay
    elif days_stay > 15:
        discount = price * 50/100 * days_stay
elif type_room == "president apartment":
    price = 35
    if days_stay < 10:
        discount = price * 10/100 * days_stay
    elif 10 <= days_stay <= 15:
        discount = price * 15/100 * days_stay
    elif days_stay > 15:
        discount = price * 20/100 * days_stay

# If discount
if discount:
    price_stay = (days_stay * price) - discount
else:
    price_stay = days_stay * price
# 3. Feedback
if feedback == "positive":
    discount_feedback = price_stay * 25/100
    price_stay = price_stay + discount_feedback
elif feedback == "negative":
    discount_feedback = price_stay * 10/100
    price_stay = price_stay - discount_feedback
# 4. Print
print(f'{price_stay:.2f}')