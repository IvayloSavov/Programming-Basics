n = int(input())

first_m = n % 10
second_m = n // 10 % 10
third_m = n // 100 % 10

for first in range (1, first_m+1):
    for second in range (1, second_m+1):
        for third in range (1, third_m+1):
            print(f"{first} * {second} * {third} = {first * second * third};")