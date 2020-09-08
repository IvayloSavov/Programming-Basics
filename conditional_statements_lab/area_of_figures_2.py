from math import pi

shape = input()
area = 0
is_valid = True

#слагаме area, за да не се чупи, ако сложим друга фигура
if shape == 'square':
    side = float(input())
    area = side * side
elif shape == 'rectangle':
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
elif shape == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2
elif shape == 'circle':
    radius = float(input())
    area = radius * radius * pi
else:
    print('not a shape')
    is_valid = False
    # слагаме този else за да не се чупи ако въведем друга фигура, разлчина от дадените

if is_valid:
    print(f'{area:.3f}')

#може принтът да е вътре в elif или извън него.