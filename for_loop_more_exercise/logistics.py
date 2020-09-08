from sys import maxsize
number_merchandises = int(input())
total_money = 0
tons_with_van = 0
tons_with_truck = 0
tons_with_train = 0
total_tons = 0

for merchandise in range (1, number_merchandises + 1):
    tons_merchandise = int(input())
    total_tons += tons_merchandise
    if tons_merchandise <= 3:
        tons_with_van += tons_merchandise
        price = 200 * tons_merchandise
        total_money += price
    elif 4 <= tons_merchandise <= 11:
        tons_with_truck += tons_merchandise
        price = 175 * tons_merchandise
        total_money += price
    elif 12 <= tons_merchandise <= maxsize:
        tons_with_train += tons_merchandise
        price = 120 * tons_merchandise
        total_money += price

print(f"{total_money / total_tons:.2f}")
print(f"{tons_with_van/total_tons * 100:.2f}%")
print(f"{tons_with_truck/total_tons * 100:.2f}%")
print(f"{tons_with_train/total_tons * 100:.2f}%")
