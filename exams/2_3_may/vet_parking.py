number_days = int(input())
number_hours = int(input())
total = 0
for day in range(1, number_days+1):
    price_day = 0
    for hours in range (1, number_hours+1):
        if day % 2 == 0 and hours % 2 == 1:
            price = 2.50
            price_day += price
        elif day % 2 == 1 and hours % 2 == 0:
            price = 1.25
            price_day += price
        else:
            price = 1.00
            price_day += price
    total += price_day
    print(f"Day: {day} - {price_day:.2f} leva")
print(f"Total: {total:.2f} leva")