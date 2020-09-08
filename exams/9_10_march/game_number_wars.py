# 1. Read input data
name_first_player = input()
name_second_player = input()
command = input()
points_first_player = 0
points_second_player = 0
is_number_wars_first = False
is_number_wars_second = False
while command != "End of game":
    card_first_player = int(command)
    card_second_player = int(input())
    if card_first_player > card_second_player:
        points = card_first_player - card_second_player
        points_first_player += points

    elif card_second_player > card_first_player:
        points = card_second_player - card_first_player
        points_second_player += points

    elif card_first_player == card_second_player:
        card_first_player = int(input())
        card_second_player = int(input())
        while is_number_wars_first == False and is_number_wars_second == False:
            if card_first_player > card_second_player:
                is_number_wars_first = True
                break
            elif card_second_player > card_first_player:
                is_number_wars_second = True
                break
            elif card_first_player == card_second_player:
                card_first_player = int(input())
                card_second_player = int(input())
    if is_number_wars_first == False and is_number_wars_second == False:
        command = input()
    else:
        break


if command == "End of game":
    print(f"{name_first_player} has {points_first_player} points")
    print(f"{name_second_player} has {points_second_player} points")
elif is_number_wars_first:
    print("Number wars!")
    print(f"{name_first_player} is winner with {points_first_player} points")
elif is_number_wars_second:
    print("Number wars!")
    print(f"{name_second_player} is winner with {points_second_player} points")
