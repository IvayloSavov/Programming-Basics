town_name = input()
type_packet = input()
VIP_card = input()
days = int(input())
is_else = False
if town_name == "Bansko" or town_name == "Borovets":
    if type_packet == "noEquipment":
        price = 80
        if VIP_card == "yes":
            price *= 95/100
    elif type_packet == "withEquipment":
        price = 100
        if VIP_card == "yes":
            price *= 90/100
    else:
        is_else = True
        print("Invalid input!")

elif town_name == "Varna" or town_name == "Burgas":
    if type_packet == "noBreakfast":
        price = 100
        if VIP_card == "yes":
            price *= 93/100
    elif type_packet == "withBreakfast":
        price = 130
        if VIP_card == "yes":
            price *= 88/100
    else:
        is_else = True
        print("Invalid input!")
else:
    is_else = True
    print("Invalid input!")

if days > 7:
    days -= 1

if not is_else:
    if days < 1:
        print("Days must be positive number!")
    else:
        total_price = days * price
        print(f"The price is {total_price:.2f}lv! Have a nice time!")




