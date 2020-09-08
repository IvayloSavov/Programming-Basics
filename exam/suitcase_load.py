capacity = float(input())
command = input()
count_suitcases = 0
count = 0

while command != "End":
    count += 1
    volume_luggage = float(command)
    if count % 3 == 0:
        volume_luggage *= 110/100
    if capacity >= volume_luggage:
        capacity -= volume_luggage
        count_suitcases += 1
    else:
        break
    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {count_suitcases} suitcases loaded.")
