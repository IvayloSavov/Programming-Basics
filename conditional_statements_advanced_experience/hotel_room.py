# 1. Read input data
month = input()
number_nights = int(input())
price_studio = 0
price_apartment = 0
# 2. Prices
if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if number_nights > 14:
        discount = price_studio * 30/100
        price_studio = price_studio - discount
    elif number_nights > 7:
        discount = price_studio * 5/100
        price_studio = price_studio - discount
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if number_nights > 14:
        discount = price_studio * 20/100
        price_studio = price_studio - discount
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
if number_nights > 14:
    discount_apartment = price_apartment * 10/100
    price_apartment = price_apartment - discount_apartment
# 3 Total prices
total_apartment = number_nights * price_apartment
total_studio = number_nights * price_studio
# 4. Print
print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
