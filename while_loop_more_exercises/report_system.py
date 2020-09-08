needed_sum = int(input())
collected_sum = 0
transaction = 0
cash_trans = 0
card_trans = 0
client_cash = 0
client_card = 0
fail = False

while collected_sum < needed_sum:
    price = input()
    transaction += 1
    if price == "End":
        fail = True
        break
    else:
        price = int(price)
    if transaction % 2 == 1:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            client_cash += 1
            cash_trans += price
            collected_sum += price
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            collected_sum += price
            client_card += 1
            card_trans += price

if collected_sum >= needed_sum:
    print(f"Average CS: {cash_trans / client_cash:.2f}")
    print(f"Average CC: {card_trans / client_card:.2f}")
elif fail:
    print("Failed to collect required money for charity.")
