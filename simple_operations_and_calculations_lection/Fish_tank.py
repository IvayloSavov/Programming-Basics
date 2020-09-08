# 1. Read input data and convert data type for the lenght of the aquarium
lenght = int(input())
# 2. Read input data and convert data type for the width fo the aquarium
width = int(input())
# 3. Read input data and convert data type for the height fo the aquarium
height = int(input())
# 4. Read input data and convert data type for the percent busy volume fo the aquarium
percent_busy_volume = float(input()) / 100
# 5. Calculate the square area of the parallelepiped
S = lenght * width
# 6. Calculate the V of the parallelepiped
V = S * height
# 7. Calculate the deduction
deduction = V * percent_busy_volume
# 8. Calculate the liters in the aquarium (V of the parallelepiped) after deduction of the percent busy volume and calculate
# and converting from cm3 to liters
liters_in_the_aquarium = (V - deduction)/1000
# 10. Print the calculated liters
print(f'{liters_in_the_aquarium:.3f}')
