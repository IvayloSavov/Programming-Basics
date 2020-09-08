price_cookies = 1.50
price_cake = 7.80
price_waffles = 2.30
total_sum = 0
total_sweets = 0
count = 0
number_participants = int(input())

for participants in range (1, number_participants+1):
    command = input()
    first_time_for_this_baker = 0
    count_cookies = 0
    count_cakes = 0
    count_waffles = 0
    name_participant = str(command)
    while command != "Stop baking!":
        first_time_for_this_baker += 1
        if first_time_for_this_baker == 1:
            type_sweets = input()
        else:
            type_sweets = str(command)
        number_baked_sweets = int(input())

        if type_sweets == "cookies":
            count_cookies += number_baked_sweets
            money = number_baked_sweets * price_cookies
            total_sum += money
            total_sweets += number_baked_sweets
        elif type_sweets == "cakes":
            count_cakes += number_baked_sweets
            money = number_baked_sweets * price_cake
            total_sum += money
            total_sweets += number_baked_sweets
        elif type_sweets == "waffles":
            count_waffles += number_baked_sweets
            money = number_baked_sweets * price_waffles
            total_sum += money
            total_sweets += number_baked_sweets
        command = input()
    print(f"{name_participant} baked {count_cookies} cookies, {count_cakes} cakes and {count_waffles} waffles.")

print(f"All bakery sold: {total_sweets}")
print(f"Total sum for charity: {total_sum:.2f} lv.")


