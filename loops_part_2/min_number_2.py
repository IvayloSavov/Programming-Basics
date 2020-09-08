from sys import maxsize
number = int(input())
smallest_number = maxsize

for count in range(number):
    current_number = int(input())
    if current_number < smallest_number:
        smallest_number = current_number

print(smallest_number)