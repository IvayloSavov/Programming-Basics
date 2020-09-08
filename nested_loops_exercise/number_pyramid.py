n = int(input())
current_row = 1
is_current_biggest_than_n = False
for row in range (1, n+1):
    for numbers_in_row in range (1, row + 1):
        if current_row > n:
            is_current_biggest_than_n = True
            break
        print(str(current_row) + ' ', end="")
        current_row += 1
    if is_current_biggest_than_n:
        break
    print()