# 1. Read input data
size_eggs = input()
color_eggs = input()
number_lots = int(input())
price = 1
# 2. If checks
if color_eggs == "Red":
    if size_eggs == "Large":
        price = 16
    elif size_eggs == "Medium":
        price = 13
    elif size_eggs == "Small":
        price = 9
elif color_eggs == "Green":
    if size_eggs == "Large":
        price = 12
    elif size_eggs == "Medium":
        price = 9
    elif size_eggs == "Small":
        price = 8
elif color_eggs == "Yellow":
    if size_eggs == "Large":
        price = 9
    elif size_eggs == "Medium":
        price = 7
    elif size_eggs == "Small":
        price = 5
# 3. Total price
total_price = number_lots * price
production_expenses = total_price * 0.35
total_price -= production_expenses
print(f"{total_price:.2f} leva.")
