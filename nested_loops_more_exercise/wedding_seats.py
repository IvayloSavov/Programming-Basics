last_sector = input()
number_row_first_sector = int(input())
number_odd_row_seats = int(input())
last_sector_ord = ord(last_sector)
count_seats = 0

for sector in range(65, last_sector_ord+1):
    if sector != 65:
        number_row_first_sector += 1
    for row in range(1, number_row_first_sector+1):
        if row % 2 == 0:
            number_even_row_seats = number_odd_row_seats + 2
            for seats in range(97, 97 + number_even_row_seats):
                count_seats += 1
                print(f"{chr(sector)}{row}{chr(seats)}")
        elif row % 2 == 1:
            for seats in range(97, 97 + number_odd_row_seats):
                count_seats += 1
                print(f"{chr(sector)}{row}{chr(seats)}")
print(count_seats)