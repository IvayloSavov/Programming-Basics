n = int(input())

n_str = str(n)
first_m = n_str[2]
second_m = n_str[1]
third_m = n_str[0]

first_m = int(first_m)
second_m = int(second_m)
third_m = int(third_m)

for first in range (1, first_m+1):
    for second in range (1, second_m+1):
        for third in range (1, third_m+1):
            print(f"{first} * {second} * {third} = {first * second * third};")