# 1. Read input data
number_guests = int(input())
price_for_one_guest = float(input())
money_desi = float(input())
# 2. Discounts
if 10 <= number_guests <= 15:
    discount = price_for_one_guest * 0.15 * number_guests
    money_party = (number_guests * price_for_one_guest) - discount
elif 15 <= number_guests <= 20:
    discount = price_for_one_guest * 0.20 * number_guests
    money_party = (number_guests * price_for_one_guest) - discount
elif number_guests > 20:
    discount = price_for_one_guest * 0.25 * number_guests
    money_party = (number_guests * price_for_one_guest) - discount
else:
    money_party = number_guests * price_for_one_guest
# 4. Price cake
price_cake = money_desi * 0.1
money_party = money_party + price_cake
# 5. Money Desi
money_desi = (money_desi - money_party)
# 6. If they are enough
if money_desi >= 0:
    print(f'It is party time! {abs(money_desi):.2f} leva left.')
else:
    print(f'No party! {abs(money_desi):.2f} leva needed.')