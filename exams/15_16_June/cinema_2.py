seats = int(input())
price_ticket = 5.00
is_movie_time = False
is_full = True
income = 0
money = 0
command = input()
while command != "Movie time!": # while seats > 0: тогава command ще се провери дали не е Movie time!
    number_people = int(command)
    if number_people > seats:
        is_full = True
        break
    else:
        money = price_ticket * number_people
    if number_people % 3 == 0:
        money -= 5
    income += money
    seats -= number_people
    command = input()

if command == "Movie time!":
    print(f"There are {seats} seats left in the cinema.")
    print(f"Cinema income - {round(income)} lv.")
elif is_full:
    print("The cinema is full.")
    print(f"Cinema income - {round(income)} lv.")