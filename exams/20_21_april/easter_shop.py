# 1. Read input data
eggs = int(input())
eggs_sold = 0

for day in range(1000000000000000000):
    buy_fill = input()
    if buy_fill != "Close":
        number_eggs = int(input())
    if buy_fill == "Buy":
        if number_eggs > eggs:
            break
        else:
            eggs -= number_eggs
            eggs_sold += number_eggs
    elif buy_fill == "Fill":
        eggs += number_eggs
    elif buy_fill == "Close":
        break


if buy_fill == "Close":
    print(f"Store is closed!\n{eggs_sold} eggs sold.")
elif number_eggs > eggs:
    print(f"Not enough eggs in store!\nYou can buy only {eggs}.")
