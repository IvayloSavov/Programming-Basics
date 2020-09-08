# 1. Read input data
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
# 2. Calculate the lenght and width
lenght = abs(x1-x2)
width = abs(y1-y2)
# 3. Calculate the square are and the perimeter
square_area = lenght * width
perimeter = (lenght+width)*2
# 4. Print the results
print (f'{square_area:.2f}')
print (f'{perimeter:.2f}')