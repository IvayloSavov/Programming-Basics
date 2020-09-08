from math import ceil
number_people = int(input())
price_entrance = float(input())
price_bed = float(input())
price_umbrella = float(input())

price_entrance_total = number_people * price_entrance
price_umbrella_total = ceil(number_people / 2) * price_umbrella
price_bed_total = ceil(number_people * 75/100) * price_bed

total = price_entrance_total + price_umbrella_total + price_bed_total

print(f"{total:.2f} lv.")