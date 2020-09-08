type_cruise = input()
type_suite = input()
number_nights = int(input())


if type_cruise == "Mediterranean":
    if type_suite == "standard cabin":
        price = 27.50
    elif type_suite == "cabin with balcony":
        price = 30.20
    elif type_suite == "apartment":
        price = 40.50

elif type_cruise == "Adriatic":
    if type_suite == "standard cabin":
        price = 22.99
    elif type_suite == "cabin with balcony":
        price = 25.00
    elif type_suite == "apartment":
        price = 34.99

elif type_cruise == "Aegean":
    if type_suite == "standard cabin":
        price = 23.00
    elif type_suite == "cabin with balcony":
        price = 26.60
    elif type_suite == "apartment":
        price = 39.80

total_price = price * number_nights * 4
if number_nights > 7:
    total_price *= 75/100

print(f"Annie's holiday in the {type_cruise} sea costs {total_price:.2f} lv.")