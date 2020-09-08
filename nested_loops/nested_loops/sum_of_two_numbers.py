start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
number_operation = 0
is_magic = False

for number_1 in range(start_interval, end_interval+1):
    for number_2 in range(start_interval, end_interval + 1):
        number_operation += 1
        if number_1 + number_2 == magic_number:
            is_magic = True
            break
    if is_magic:
        break
if is_magic:
    print(f"Combination N:{number_operation} ({number_1} + {number_2} = {magic_number})")
else:
    print(f"{number_operation} combinations - neither equals {magic_number}")