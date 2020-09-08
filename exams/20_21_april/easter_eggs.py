from sys import maxsize
red = 0
orange = 0
blue = 0
green = 0
max_eggs_of_color = ""
name_max_eggs = ""
number_eggs = int(input())

for egg in range (1, number_eggs+1):
    color_egg = input()
    if color_egg == "red":
        red += 1
    elif color_egg == "orange":
        orange += 1
    elif color_egg == "blue":
        blue += 1
    elif color_egg == "green":
        green += 1

if red > orange and red > blue and red > green:
    max_eggs_of_color = "red"

if orange > red and orange > blue and orange > green:
    max_eggs_of_color = "orange"

if blue > red and blue > orange and blue > green:
    max_eggs_of_color = "blue"

if green > red and green > orange and green > blue:
    max_eggs_of_color = "green"

colors = max(red, orange, blue, green)


print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {colors} -> {max_eggs_of_color}")