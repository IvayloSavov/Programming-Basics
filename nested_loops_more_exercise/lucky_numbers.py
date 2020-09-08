N = int(input())

for first_number in range(1, 9+1):
    for second_number in range(1, 9+1):
        for third_number in range(1, 9+1):
            for fourth_number in range(1, 9+1):
                if first_number + second_number == third_number + fourth_number and N % (first_number+second_number) == 0:
                        print(str(first_number) + str(second_number) + str(third_number) + str(fourth_number), end= " ")