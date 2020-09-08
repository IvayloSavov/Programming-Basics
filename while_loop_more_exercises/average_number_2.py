n = int(input())
count = 0
total = 0
while count < n:
    count += 1
    number = int(input())
    total += number

print(f"{total / n:.2f}")