start = input()
stop = input()
letter_pass = input()
count = 0
start_ord = ord(start)
stop_ord = ord(stop)

for first_letter in range(start_ord, stop_ord + 1):
    for second_letter in range(start_ord, stop_ord + 1):
        for third_letter in range(start_ord, stop_ord + 1):
            if chr(first_letter) != letter_pass and chr(second_letter) != letter_pass and chr(third_letter) != letter_pass:
                count += 1
                print(chr(first_letter) + chr(second_letter) + chr(third_letter), end=" ")

print(count)