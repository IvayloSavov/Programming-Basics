number_passenger_departure = int(input())
number_stops = int(input())


total_passengers = number_passenger_departure

for stop in range (1, number_stops+1):
    passenger_out = int(input())
    passenger_in = int(input())

    total_passengers += passenger_in
    total_passengers -= passenger_out

    if stop % 2 == 1:
        total_passengers += 2
    else:
        total_passengers -= 2

print(f"The final number of passengers is : {total_passengers}")