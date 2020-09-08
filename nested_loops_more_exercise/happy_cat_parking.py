number_days = int(input())
hours_per_day = int(input())
total = 0

for day in range(1, number_days + 1):
    money_per_day = 0
    for hour in range (1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            price = 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1.00
        money_per_day += price

    print(f"Day: {day} - {money_per_day:.2f} leva")
    total += money_per_day

print(f"Total: {total:.2f} leva")