start_first_couple = int(input())
start_second_couple = int(input())

difference_start_end_first_couple = int(input())
difference_start_end_second_couple = int(input())

end_first_couple = start_first_couple + difference_start_end_first_couple
end_second_couple = start_second_couple + difference_start_end_second_couple

is_first_couple_prime_number = False
is_second_couple_prime_number = False

for first_couple in range(start_first_couple, end_first_couple + 1):
    for second_couple in range(start_second_couple, end_second_couple + 1):
        is_first_couple_prime_number = False
        is_second_couple_prime_number = False
        if first_couple > 1 and second_couple > 1:
            for i in range(2, first_couple):
                if first_couple % i == 0:
                    break
            else:
                is_first_couple_prime_number = True

            for n in range(2, second_couple):
                if second_couple % n == 0:
                    break
            else:
                is_second_couple_prime_number = True

        if is_first_couple_prime_number and is_second_couple_prime_number:
            print(f"{first_couple}{second_couple}")
