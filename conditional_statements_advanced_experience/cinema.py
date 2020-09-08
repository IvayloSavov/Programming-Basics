# 1. Read input data
type_of_filmshow = input()
number_row = int(input())
number_column = int(input())
price = 0
income = 0
# 2. Type of filmshow
if type_of_filmshow == "Premiere":
    price = 12.00
elif type_of_filmshow == "Normal":
    price = 7.50
elif type_of_filmshow == "Discount":
    price = 5.00
# 3. Capacity
capacity = number_row * number_column
income = capacity * price
# 4. Print
print(f'{income:.2f} leva')