first_num = int(input())
second_num = int(input())
operator = (input())
result = 0
odd_or_even = ""
if operator == "+" or operator == '*' or operator == "-":
    if operator == "+":
        result = first_num + second_num
    elif operator == "*":
        result = first_num * second_num
    else:
        result = first_num - second_num

    if result % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{first_num} {operator} {second_num} = {result} - {odd_or_even}")
else:
    if operator == "/":
        if second_num:
            result = first_num / second_num
            print(f"{first_num} {operator} {second_num} = {result:.2f}")
        else:
            print(f"Cannot divide {first_num} by zero")

    else:
        if second_num:
            result = first_num % second_num
            print(f"{first_num} {operator} {second_num} = {result}")
        else:
            print(f"Cannot divide {first_num} by zero")