number_bottles = int(input())
one_bottle = 750
total_faith = number_bottles * 750
used_faith = 0
count_charge = 0
number_plates = 0
number_pots = 0

command = input()
while command != "End":
    count_charge += 1
    number_dishes = int(command)
    if count_charge % 3 == 0:
        number_pots += number_dishes
        used_faith += (number_dishes * 15)
    else:
        number_plates += number_dishes
        used_faith += (number_dishes * 5)
    if used_faith > total_faith:
        break
    else:
        command = input()

needed_left_detergent = abs(used_faith - total_faith)
if total_faith >= used_faith:
    print(f"Detergent was enough!")
    print(f"{number_plates} dishes and {number_pots} pots were washed.")
    print(f"Leftover detergent {needed_left_detergent} ml.")
else:
    print(f"Not enough detergent, {needed_left_detergent} ml. more necessary!")