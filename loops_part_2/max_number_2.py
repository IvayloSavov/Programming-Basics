from sys import maxsize
count_number = int(input())
biggest_number = -maxsize
count = 0
for count in range(count_number):
    number = int(input())
    if number > biggest_number:
        biggest_number = number

print(biggest_number)