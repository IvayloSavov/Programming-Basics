money_in_voucher = int(input())
command = input()
number_tickets = 0
number_other_products = 0

while command != "End":
    type_purchase = str(command)
    length_type_purchase = len(type_purchase)
    if length_type_purchase > 8:
        first_symbol = type_purchase[0]
        second_symbol = type_purchase[1]
        ascii_first = ord(first_symbol)
        ascii_second = ord(second_symbol)
        price = ascii_first + ascii_second
        if price > money_in_voucher:
            break
        else:
            money_in_voucher -= price
            number_tickets += 1
    else:
        first_symbol = type_purchase[0]
        second_symbol = type_purchase[1]
        ascii_first = ord(first_symbol)
        price = ascii_first
        if price > money_in_voucher:
            break
        else:
            money_in_voucher -= price
            number_other_products += 1
    if money_in_voucher <= 0:
        break
    else:
        command = input()

print(number_tickets)
print(number_other_products)