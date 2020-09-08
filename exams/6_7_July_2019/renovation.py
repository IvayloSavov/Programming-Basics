from math import ceil
height_wall = int(input())
width_wall = int(input())
percent_not_painting = int(input())
command = input()
paintings = 0
is_painted = False

square_total = height_wall * width_wall * 4
square_total = square_total - (square_total * percent_not_painting / 100)
square_total = ceil(square_total)

while command != "Tired!":
    litres_paint = int(command)
    paintings += 1
    square_total -= litres_paint * 1

    if square_total <= 0:
        is_painted = True
        break
    else:
        command = input()
if command == "Tired!":
    print(f"{square_total} quadratic m left." )
elif is_painted:
    if square_total < 0:
        print(f"All walls are painted and you have {abs(square_total)} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
