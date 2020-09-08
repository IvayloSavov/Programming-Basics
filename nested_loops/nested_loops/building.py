number_floors = int(input())
number_rooms = int(input())

for current_floor in range(number_floors, 0, -1):
    for current_room in range(number_rooms):
        if current_floor == number_floors:
            print(f"L{current_floor}{current_room}", end=" ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end=" ")
        else:
            print(f"A{current_floor}{current_room}", end=" ")
    print()


