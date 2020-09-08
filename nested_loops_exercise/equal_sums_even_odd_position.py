first_number = int(input())
second_number = int(input())


for number in range (first_number, second_number + 1):
    number_to_str = str(number)
    index = 0
    even_sum = 0
    odd_sum = 0
    for digit in number_to_str:
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

        index += 1
    if even_sum == odd_sum:
        print(number, end=" ")