N = int(input())
for number in range(1111, 9999+1):
    number = str(number)
    count = 0
    for digit in number:
        if int(digit) == 0:
            pass
        elif N % int(digit) == 0:
            count += 1
    if count == 4:
        print(number, end= " ")