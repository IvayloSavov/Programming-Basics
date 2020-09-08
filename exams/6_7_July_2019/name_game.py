from sys import maxsize
command = input()
points_winner = -maxsize
winner_name = ""

while command != "Stop":
    name_player = str(command)
    len_name = len(name_player)
    points = 0
    for i in range(len_name):
        number = int(input())
        current_char = name_player[i]
        if number == ord(current_char):
            points += 10
        else:
            points += 2

    if points >= points_winner:
        points_winner = points
        winner_name = name_player

    command = input()

print(f"The winner is {winner_name} with {points_winner} points!")