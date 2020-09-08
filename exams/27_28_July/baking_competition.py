price_cookies = 1.50
price_cakes = 7.80
price_pancakes = 2.30
total_sweets = 0
total_money = 0
number_participants = int(input())


for participant in range(1, number_participants+1):
    name_participant = input()
    cookies = 0
    cakes = 0
    waffles = 0
    command = input()
    while command != "Stop baking!":
        type_sweets = str(command)
        number_sweets = int(input())
        if type_sweets == "cookies":
            cookies += number_sweets
            total_sweets += number_sweets
            money = number_sweets * price_cookies
            total_money += money

        elif type_sweets == "cakes":
            cakes += number_sweets
            total_sweets += number_sweets
            money = number_sweets * price_cakes
            total_money += money

        elif type_sweets == "waffles":
            waffles += number_sweets
            total_sweets += number_sweets
            money = number_sweets * price_pancakes
            total_money += money
        command = input()
    print(f"{name_participant} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")

print(f"All bakery sold: {total_sweets}")
print(f"Total sum for charity: {total_money:.2f} lv.")
