number_1_lev = int(input())
number_2_lev = int(input())
number_5_lev = int(input())
client_sum_entrance = int(input())

for lev_1 in range(number_1_lev + 1):
    for lev_2 in range(number_2_lev + 1):
        for lev_5 in range(number_5_lev + 1):
            if (lev_1 * 1 + lev_2 * 2 + lev_5 * 5) == client_sum_entrance:
                print(f"{lev_1} * 1 lv. + {lev_2} * 2 lv. + {lev_5} * 5 lv. = {client_sum_entrance} lv.")