start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combination_found = False
combination_number = 0

for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        combination_number += 1
        if first_number + second_number == magic_number:
            combination_found = True
            print(f"Combination N:{combination_number} ({first_number} + {second_number} = {magic_number})")
            break

    if combination_found:
        break

if not combination_found:
    print(f"{combination_number} combinations - neither equals {magic_number}")