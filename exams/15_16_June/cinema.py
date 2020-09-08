# 1. Read input data
seats = int(input())
price_ticket = 5.00
is_movie_time = False
is_full = True
income = 0
money = 0
for taken_seats in range(1, seats+1):
    number_people = input()
    if number_people == "Movie time!":
        is_movie_time = True
        break
    else:
        number_people = int(number_people)
        if number_people > seats:
            is_full = True
            break
        else:
            money = price_ticket * number_people
        if number_people % 3 == 0:
            money -= 5
        income += money
        seats -= number_people
if is_movie_time:
    print(f"There are {seats} seats left in the cinema.")
    print(f"Cinema income - {round(income)} lv.")
elif is_full:
    print("The cinema is full.")
    print(f"Cinema income - {round(income)} lv.")