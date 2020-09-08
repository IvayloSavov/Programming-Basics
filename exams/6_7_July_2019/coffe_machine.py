drink = input()
sugar = input()
number_drinks = int(input())

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * 65/100
    elif sugar == "Normal":
        price = 1.00
    elif sugar == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1.00 * 65 / 100
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * 65 / 100
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total = number_drinks * price

if drink == "Espresso" and number_drinks >= 5:
    total *= 75/100

if total > 15:
    total*= 80/100

print(f"You bought {number_drinks} cups of {drink} for {total:.2f} lv.")