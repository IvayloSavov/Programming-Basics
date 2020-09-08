# 1. Input lenght of the aquarium
lenght = int(input())
# 2. Input width fo the aquarium
width = int(input())
# 3. Input height fo the aquarium
height = int(input())
# 4. Input percent busy volume fo the aquarium
percent_busy_volume = 0.17
# 5. Calculate the square of the parallelepiped
S = lenght * width
# 6. Calculate the liters in the aquarium (V of the parallelepiped)
liters = S * height
# 7. Calculate the deduction
deduction = liters * percent_busy_volume
# 7. Calculate the liters in the aquarium (V of the parallelepiped) after deduction of the percent busy volume
liters_in_the_aquarium = liters - deduction
# 8. Print the calculated liters
print(liters_in_the_aquarium)