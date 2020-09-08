first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())
is_not_prime = False
for first_num in range(1, first_num_max+1):
    for second_num in range(1, second_num_max+1):
        for third_num in range(1, third_num_max+1):
            if first_num % 2 == 0 and third_num % 2 == 0 and second_num > 1:
                for i in range(2, second_num):
                    if (second_num % i) == 0:
                        break
                else:
                    print(f"{first_num} {second_num} {third_num}")
