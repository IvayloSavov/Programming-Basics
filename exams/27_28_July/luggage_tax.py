# 1. Read input data
width_luggage = int(input())
height_luggage = int(input())
deep_luggage = int(input())
is_priority = input()
taxes = 0
# 2. Volume lugagge
volume = width_luggage * height_luggage * deep_luggage
# 3. If checks
if is_priority == "true":
    if 50 <= volume <= 100:
        taxes = 0
    elif 100 <= volume <= 200:
        taxes = 10
    elif 200 <= volume <= 300:
        taxes = 20
else:
    if 50 <= volume <= 100:
        taxes = 25
    elif 100 <= volume <= 200:
        taxes = 50
    elif 200 <= volume <= 300:
        taxes = 100
# 4. Print
print(f"Luggage tax: {taxes:.2f}")
