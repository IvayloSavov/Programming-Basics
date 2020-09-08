budget = float(input())
number_serials = int(input())
total_price = 0
not_enough_money = False

for serial in range(1, number_serials + 1):
    name_serial = input()
    price_serial = float(input())
    if name_serial == "Thrones":
        price_serial *= 50/100
    elif name_serial == "Lucifer":
        price_serial *= 60/100
    elif name_serial == "Protector":
        price_serial *= 70/100
    elif name_serial == "TotalDrama":
        price_serial *= 80/100
    elif name_serial == "Area":
        price_serial *= 90/100
    total_price += price_serial


if budget >= total_price:
    print(f"You bought all the series and left with {abs(budget - total_price):.2f} lv.")
else:
    print(f"You need {abs(total_price - budget):.2f} lv. more to buy the series!")
