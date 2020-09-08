n_1 = int(input())
n_2 = int(input())

for number in range (n_1, n_2+1):
    number = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end= " ")