number_tickets = int(input())


for current_ticket in range (1, number_tickets+1):
    ticket_number = input()
    current_symbol = ticket_number[0]
    check_is_digit = current_symbol.isdigit()
    check_is_alpha = current_symbol.isalpha()
    len_check = len(ticket_number)
    if len_check == 5 or len_check == 6:
        first_symbol = ticket_number[0]
        second_symbol = ticket_number[1]
        second_symbol = ord(second_symbol)
        print(f"Seat decoded: {first_symbol}{second_symbol}")
    elif check_is_alpha:
        check_is_uppercase = ticket_number.isupper()
        if check_is_uppercase:
            first_symbol = ticket_number[0]
            second_symbol = ticket_number[1]
            third_symbol = ticket_number[2]
            print(f"Seat decoded: {first_symbol}{second_symbol}{third_symbol}")
        else:
            second_symbol = ticket_number[1]
            third_symbol = ticket_number[2]
            fourth_symbol = ticket_number[3]
            print(f"Seat decoded: {fourth_symbol}{second_symbol}{third_symbol}")
    else:
        second_symbol = ticket_number[1]
        third_symbol = ticket_number[2]
        fourth_symbol = ticket_number[3]
        print(f"Seat decoded: {fourth_symbol}{second_symbol}{third_symbol}")

