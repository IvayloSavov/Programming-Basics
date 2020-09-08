student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

command = input()
while command != "Finish":
    name_film = str(command)
    free_seats = int(input())
    bought_seats = 0
    for ticket in range (1, free_seats+1):
        type_ticket = input()
        if type_ticket == "End":
            break
        total_tickets += 1
        bought_seats += 1
        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == "kid":
            kid_tickets += 1
    print(f"{name_film} - {bought_seats / free_seats * 100:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kid_tickets/total_tickets*100:.2f}% kids tickets.")