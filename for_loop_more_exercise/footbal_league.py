capacity_stadium = int(input())
number_fans = int(input())

count_first_team = 0
count_second_team = 0
count_A = 0
count_B = 0
count_V = 0
count_G = 0

for fan in range(1, number_fans + 1):
    sector = input()
    if sector == "A":
        count_first_team += 1
        count_A += 1
    elif sector == "B":
        count_first_team += 1
        count_B += 1
    elif sector == "V":
        count_second_team += 1
        count_V += 1
    elif sector == "G":
        count_second_team += 1
        count_G += 1

print(f"{count_A/number_fans * 100:.2f}%")
print(f"{count_B/number_fans * 100:.2f}%")
print(f"{count_V/number_fans * 100:.2f}%")
print(f"{count_G/number_fans * 100:.2f}%")
print(f"{number_fans/capacity_stadium*100:.2f}%")