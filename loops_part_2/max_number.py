from sys import maxsize
count_number = int(input())
biggest_number = -maxsize
count = 0
while count < count_number:
    number = int(input())
    count += 1
    if number > biggest_number:
        biggest_number = number

print(biggest_number)

