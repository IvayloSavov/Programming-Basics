from math import floor
name_player = input()
number_played_games = int(input())
volleyball_points = 0
tennis_points = 0
badminton_points = 0
count_volleyball = 0
count_tennis = 0
count_badminton = 0

for game in range(1, number_played_games+1):
    name_game = input()
    number_points = int(input())
    if name_game == "volleyball":
        number_points *= 107 / 100
        volleyball_points += number_points
        count_volleyball += 1

    elif name_game == "tennis":
        number_points *= 105 / 100
        tennis_points += number_points
        count_tennis += 1

    elif name_game == "badminton":
        number_points *= 102 / 100
        badminton_points += number_points
        count_badminton += 1

average_volleyball = floor(volleyball_points/count_volleyball)
average_tennis = floor(tennis_points/count_tennis)
average_badminton = floor(badminton_points/count_badminton)

total_points = floor(volleyball_points + tennis_points + badminton_points)

if average_volleyball >= 75 and average_tennis >= 75 and average_badminton >= 75:
    print(f"Congratulations, {name_player}! You won the cruise games with {total_points} points.")
else:
    print(f"Sorry, {name_player}, you lost. Your points are only {total_points}.")