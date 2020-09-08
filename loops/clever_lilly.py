age_Lilly = int(input())
price_washing_machine = float(input())
price_toy = int(input())

money_to_recieve = 0
savings = 0
toys = 0

for years in range (1, age_Lilly + 1):
    if years == 2:
        money_to_recieve = 10
        savings += money_to_recieve
        savings -= 1
    elif years % 2 == 0:
        money_to_recieve += 10
        savings += money_to_recieve
        savings -= 1
    else:
        toys += 1

money_toys = toys * price_toy
total_money = savings + money_toys

money_left_needed = abs(total_money - price_washing_machine)

if total_money >= price_washing_machine:
    print(f"Yes! {money_left_needed:.2f}")
else:
    print(f"No! {money_left_needed:.2f}")