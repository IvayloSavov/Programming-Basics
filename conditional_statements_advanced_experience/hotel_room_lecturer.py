month = input()
count_nights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if count_nights > 14:
        price_studio *= 0.95
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if count_nights > 14:
        price_studio *= 0.80
else:
    price_studio = 76
    price_apartment = 77

if count_nights > 14:
    price_apartment *= 0.9

print(f'Apartment: {price_apartment*count_nights:.2f} lv.')
print(f'Studio: {price_studio*count_nights:.2f} lv.')
