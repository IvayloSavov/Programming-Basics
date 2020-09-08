start = int(input())
stop = int(input())

for first_number in range (start, stop + 1):
    for second_number in range (start, stop + 1):
        for third_number in range (start, stop + 1):
            for fourth_number in range (start, stop + 1):
                if first_number > fourth_number and (second_number + third_number) % 2 == 0:
                    if first_number % 2 == 0 and fourth_number % 2 == 1:
                        print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                    elif first_number % 2 == 1 and fourth_number % 2 == 0:
                        print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")