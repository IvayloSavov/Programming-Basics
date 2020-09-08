from sys import maxsize
command = input()
best_flight_number = ""
best_price = 0
low_minutes_stay = maxsize
ticket_found = False
while command != "End":
    flight_number = str(command)
    price = float(input())
    minutes_stay = int(input())
    if minutes_stay < low_minutes_stay:
        best_flight_number = flight_number
        best_price = price * 1.96
        low_minutes_stay = minutes_stay
        ticket_found = True
        hours = low_minutes_stay // 60
        minutes_stay_final = low_minutes_stay % 60

    command = input()

if ticket_found:
    print(f"Ticket found for flight {best_flight_number} costs {best_price:.2f} leva with {hours}h {minutes_stay_final}m stay")