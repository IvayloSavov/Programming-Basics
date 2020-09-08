from math import ceil
type_sushi = input()
name_restaurant = input()
number_portions = int(input())
delivery = input()
is_invalid_restaurant = False
price = 1

if name_restaurant == "Sushi Zone":
    if type_sushi == "sashimi":
        price = 4.99
    elif type_sushi == "maki":
        price = 5.29
    elif type_sushi == "uramaki":
        price = 5.99
    elif type_sushi == "temaki":
        price = 4.29

elif name_restaurant == "Sushi Time":
    if type_sushi == "sashimi":
        price = 5.49
    elif type_sushi == "maki":
        price = 4.69
    elif type_sushi == "uramaki":
        price = 4.49
    elif type_sushi == "temaki":
        price = 5.19

elif name_restaurant == "Sushi Bar":
    if type_sushi == "sashimi":
        price = 5.25
    elif type_sushi == "maki":
        price = 5.55
    elif type_sushi == "uramaki":
        price = 6.25
    elif type_sushi == "temaki":
        price = 4.75

elif name_restaurant == "Asian Pub":
    if type_sushi == "sashimi":
        price = 4.50
    elif type_sushi == "maki":
        price = 4.80
    elif type_sushi == "uramaki":
        price = 5.50
    elif type_sushi == "temaki":
        price = 5.50

else:
    print(f"{name_restaurant} is invalid restaurant!")
    is_invalid_restaurant = True



if delivery == "Y":
    price_order = price * number_portions
    price_order *= 120/100
    price_order = ceil(price_order)
else:
    price_order = price * number_portions
    price_order = ceil(price_order)

if not is_invalid_restaurant:
    print(f"Total price: {price_order} lv.")