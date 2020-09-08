money = float(input())
year_to_live = int(input())
years_Ivan = 18
needed_money = 0

for year in range(1800, year_to_live + 1):
    if year != 1800:
        years_Ivan += 1
    if year % 2 == 0:
        needed_money += 12000
    else:
        needed_money += 12000 + (50 * years_Ivan)

money_left_needed = abs(money - needed_money)
if money >= needed_money:
    print(f"Yes! He will live a carefree life and will have {money_left_needed:.2f} dollars left.")
else:
    print(f"He will need {money_left_needed:.2f} dollars to survive.")