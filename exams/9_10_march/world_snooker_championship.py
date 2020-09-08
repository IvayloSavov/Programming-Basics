# 1. Read input data
stage_of_championship = input()
type_ticket = input()
number_tickets = int(input())
photo_trophy = input()
price_ticket = 1
price_photo = 40
# 2. If - prices
if stage_of_championship == "Quarter final":
    if type_ticket == "Standard":
        price_ticket = 55.50
    elif type_ticket == "Premium":
        price_ticket = 105.20
    elif type_ticket == "VIP":
        price_ticket = 118.90
elif stage_of_championship == "Semi final":
    if type_ticket == "Standard":
        price_ticket = 75.88
    elif type_ticket == "Premium":
        price_ticket = 125.22
    elif type_ticket == "VIP":
        price_ticket = 300.40
elif stage_of_championship == "Final":
    if type_ticket == "Standard":
        price_ticket = 110.10
    elif type_ticket == "Premium":
        price_ticket = 160.66
    elif type_ticket == "VIP":
        price_ticket = 400.00
# 3. total
total = price_ticket * number_tickets
# 4. Discount
if total > 4000:
    total = total * 0.75
    price_photo = 0
elif total > 2500:
    total = total * 0.90
# 5. Photo
if photo_trophy == "Y":
    total = total + (price_photo*number_tickets)
# 6. Print
print(f"{total:.2f}")