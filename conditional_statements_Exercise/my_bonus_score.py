# 1. Read input data
number = int(input())
bonus = 0

if points <= 100:
    bonus = 5
elif points > 100: #ако са две elif ще приеме и двете ако са над 1000
    bonus = points * 0.20
elif points > 1000:
    bonus = points * 0.10

# 2. Extra bonus points
if points % 2 == 0:
    bonus_points = 1 + bonus_points
elif points % 10 == 5:
    bonus_points = 2 + bonus_points

points = points + bonus_points

print(bonus_points)
print(points)