from sys import maxsize
number = int(input())
smallest_number = maxsize
count = 0
while count < number:
    current_number = int(input())
    count += 1
    if current_number < smallest_number:
        smallest_number = current_number

print(smallest_number)