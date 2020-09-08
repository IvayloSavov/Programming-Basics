# 1. Read input data
type_cruise = input()
type_cabin = input()
number_nights = int(input())
number_person = 4
# 2. Check if cruise and cabin
if type_cruise == "Mediterranean":
    if type_cabin == "standard cabin":
        price = 27.50
    elif type_cabin == "cabin with balcony":
        price = 30.20
    elif type_cabin == "apartment":
        price = 40.50
elif type_cruise == "Adriatic":
    if type_cabin == "standard cabin":
        price = 22.99
    elif type_cabin == "cabin with balcony":
        price = 25.00
    elif type_cabin == "apartment":
        price = 34.99
elif type_cruise == "Aegean":
    if type_cabin == "standard cabin":
        price = 23.00
    elif type_cabin == "cabin with balcony":
        price = 26.60
    elif type_cabin == "apartment":
        price = 39.80
price_holiday = price * number_nights * number_person
# 3. Check if nights
if number_nights > 7:
    discount = price_holiday * 25/100
    price_holiday -= discount
# 4. Print
print(f"Annie's holiday in the {type_cruise} sea costs {price_holiday:.2f} lv.")

