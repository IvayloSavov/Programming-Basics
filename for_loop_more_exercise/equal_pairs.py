from sys import maxsize
n = int(input())
count_equal_pairs = 0
equal_sum_pair = 0
max_difference = -maxsize
sum_previous_pair = 0

for pair in range(1, n+1):
    number_1 = int(input())
    number_2 = int(input())
    if pair == 1:
        equal_sum_pair = number_1 + number_2
        count_equal_pairs += 1
    elif number_1 + number_2 == equal_sum_pair:
        count_equal_pairs += 1
    else:
        difference = abs(sum_previous_pair - (number_1 + number_2))
        if difference > max_difference:
            max_difference = difference
    sum_previous_pair = number_1 + number_2

if count_equal_pairs == n:
    print(f"Yes, value={equal_sum_pair}")
else:
    print(f"No, maxdiff={max_difference}" )