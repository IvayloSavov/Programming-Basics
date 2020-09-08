command = input()
bought_seats = 0
tickets_bought = 0
tickets_student = 0
tickets_standard = 0
tickets_kids = 0
bought_seats_total = 0

while command != "Finish":
    name_film = str(command)
    free_seats = int(input())

    while bought_seats < free_seats:
        command_2 = input()
        if command_2 == "End":
            break
        type_ticket = str(command_2)
        if type_ticket == "student":
            tickets_student += 1
        elif type_ticket == "standard":
            tickets_standard += 1
        elif type_ticket == "kid":
            tickets_kids += 1
        bought_seats += 1

    percent_taken_seats = bought_seats / free_seats * 100
    print(f"{name_film} - {percent_taken_seats:.2f}% full.")
    bought_seats_total += bought_seats
    bought_seats = 0
    
    command = input()

if command == "Finish":
    print(f"Total tickets: {bought_seats_total}")
    print(f"{(tickets_student / bought_seats_total * 100):.2f}% student tickets.")
    print(f"{(tickets_standard / bought_seats_total * 100):.2f}% standard tickets.")
    print(f"{(tickets_kids / bought_seats_total * 100):.2f}% kids tickets.")
