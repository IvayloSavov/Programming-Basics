price_basket = 1.50
price_wreath = 3.80
price_bunny = 7.00
money_clients = 0
number_clients = int(input())

for client in range (1, number_clients + 1):
    command = input()
    count_products = 0
    money_current_client = 0
    while command != "Finish":
        product = str(command)
        count_products += 1
        if command == "basket":
            money_current_client += price_basket
        elif command == "wreath":
            money_current_client += price_wreath
        elif command == "chocolate bunny":
            money_current_client += price_bunny
        command = input()
    if count_products % 2 == 0:
        money_current_client *= 80/100
    money_clients += money_current_client
    print(f"You purchased {count_products} items for {money_current_client:.2f} leva.")

print(f"Average bill per client is: {money_clients/number_clients:.2f} leva.")
