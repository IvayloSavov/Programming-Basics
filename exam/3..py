fruit = input()
stack_size = input()
number_stack = int(input())

if fruit == "Watermelon":
    if stack_size == "small":
        price = 56
    else:
        price = 28.70
elif fruit == "Mango":
    if stack_size == "small":
        price = 36.66
    else:
        price = 19.60
elif fruit == "Pineapple":
    if stack_size == "small":
        price = 42.10
    else:
        price = 24.80
elif fruit == "Raspberry":
    if stack_size == "small":
        price = 20.00
    else:
        price = 15.20

if stack_size == "small":
    price_stack = price * 2
else:
    price_stack = price * 5
price_all_stacks = price_stack * number_stack

if price_all_stacks > 1000:
    discount = price_all_stacks * 50/100
    price_all_stacks -= discount
elif 400 <= price_all_stacks <= 1000:
    discount = price_all_stacks * 15/100
    price_all_stacks -= discount

print(f"{price_all_stacks:.2f} lv.")