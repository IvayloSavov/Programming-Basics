# 1. Read input data
day_reservation = int(input())
month_reservation = int(input())
day_arriving = int(input())
month_arriving = int(input())
day_departure = int(input())
month_departure = int(input())

price_for_one_night = False
discount = False

# 2. Number nights
number_nights = day_departure - day_arriving
# 3. If the reservation is made last month or 10 days before the arriving date
difference_days = day_arriving - day_reservation
if difference_days >= 10 or month_reservation < month_arriving:
    price_for_one_night = True
    price_for_one_night = 25
else:
    price_for_one_night = True
    price_for_one_night = 30

if month_reservation < month_arriving:
    discount = True
    discount = 25 * 0.2
    price_for_one_night -= discount

# 4. Total price
price_total = number_nights * price_for_one_night

# 5. Printing
print(f"Your stay from {day_arriving}/{month_arriving} to {day_departure}/{month_departure} will cost {price_total:.2f}")