number_moves = int(input())
count_invalid = 0
count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
total_numbers = 0

for move in range(1, number_moves + 1):
    numbers = int(input())
    if numbers < 0 or numbers > 50:
        total_numbers /= 2
        count_invalid += 1
    elif 0 <= numbers <= 9:
        numbers *= 20/100
        total_numbers += numbers
        count_0_9 += 1
    elif 10 <= numbers <= 19:
        numbers *= 30/100
        total_numbers += numbers
        count_10_19 += 1
    elif 20 <= numbers <= 29:
        numbers *= 40/100
        total_numbers += numbers
        count_20_29 += 1
    elif 30 <= numbers <= 39:
        total_numbers += 50
        count_30_39 += 1
    elif 40 <= numbers <= 50:
        total_numbers += 100
        count_40_50 += 1

print(f"{total_numbers:.2f}")
print(f"From 0 to 9: {count_0_9/number_moves * 100:.2f}%")
print(f"From 10 to 19: {count_10_19/number_moves * 100:.2f}%")
print(f"From 20 to 29: {count_20_29/number_moves * 100:.2f}%")
print(f"From 30 to 39: {count_30_39/number_moves * 100:.2f}%")
print(f"From 40 to 50: {count_40_50/number_moves * 100:.2f}%")
print(f"Invalid numbers: {count_invalid/number_moves * 100:.2f}%")
