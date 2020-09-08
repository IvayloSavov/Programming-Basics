command = input()
sum_numbers = 0

while command != "Stop":
    number = int(command)
    sum_numbers += number
    command = input()

print(sum_numbers)
