change = float(input())
number_coins = 0

while change > 0:

    while change >= 2:
        change -= 2
        number_coins += 1
        change = round(change, 2)
    while change >= 1:
        change -= 1
        number_coins += 1
        change = round(change, 2)
    while change >= 0.50:
        change -= 0.50
        number_coins += 1
        change = round(change, 2)
    while change >= 0.20:
        change -= 0.20
        number_coins += 1
        change = round(change, 2)
    while change >= 0.10:
        change -= 0.10
        number_coins += 1
        change = round(change, 2)
    while change >= 0.05:
        change -= 0.05
        number_coins += 1
        change = round(change, 2)
    while change >= 0.02:
        change -= 0.02
        number_coins += 1
        change = round(change, 2)
    while change >= 0.01:
        change -= 0.01
        number_coins += 1
        change = round(change, 2)
    # if change < 0.01:
    #     change -= 0.01
    #     number_coins += 1
print(number_coins)