needed_money = float(input())
available_money = float(input())
days_spend = 0
total_days = 0

spend_5_days = False
while available_money < needed_money:
    type_command = input()
    money_spend_save = float(input())
    total_days += 1
    if type_command == "save":
        days_spend = 0
        available_money += money_spend_save
    elif type_command == "spend":
        days_spend += 1
        if money_spend_save > available_money:
            money_spend_save = available_money
        available_money -= money_spend_save
    if days_spend >= 5:
        spend_5_days = True
        break

if spend_5_days:
    print(f"You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
