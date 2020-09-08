months = int(input())
electricity_total = 0
water_total = 0
internet_total = 0
other_total = 0
average_total = 0

for month in range(1, months + 1):
    electricity = float(input())
    water = 20
    internet = 15
    others = (electricity + water + internet) * 120/100
    electricity_total += electricity
    water_total += water
    internet_total += internet
    other_total += others
    total_month = electricity + water + internet + others
    average_total += total_month

average_total /= months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_total:.2f} lv")
print(f"Average: {average_total:.2f} lv")


