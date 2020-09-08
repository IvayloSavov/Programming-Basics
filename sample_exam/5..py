money_singer = int(input())
command = input()
money = 0
guests = 0
while command != "The restaurant is full":
    number_people = int(command)
    guests += number_people
    if number_people < 5:
        price_people = 100
    else:
        price_people = 70
    price = price_people * number_people
    money += price
    command = input()
money_left_needed = abs(money_singer - money)
if money >= money_singer:
    print(f"You have {guests} guests and {money_left_needed} leva left.")
else:
    print(f"You have {guests} guests and {money} leva income, but no singer.")

