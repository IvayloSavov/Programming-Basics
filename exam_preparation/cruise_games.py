from math import floor
name_player = input()
number_played_games = int(input())
count_volleyball = 0
count_tennis = 0
count_badminton = 0
total = 0
volleyball_points = 0
tennis_points = 0
badminton_points = 0

for current_game in range(1, number_played_games+1):
    type_game = input()
    number_points = int(input())
    if type_game == "volleyball":
        count_volleyball += 1
        bonus_points = number_points * 7/100
        number_points += bonus_points
        volleyball_points += number_points

    elif type_game == "tennis":
        count_tennis += 1
        bonus_points = number_points * 5 / 100
        number_points += bonus_points
        tennis_points += number_points

    elif type_game == "badminton":
        count_badminton += 1
        bonus_points = number_points * 2 / 100
        number_points += bonus_points
        badminton_points += number_points


average_volleyball = floor(volleyball_points / count_volleyball)
average_tennis = floor(tennis_points / count_tennis)
average_badminton = floor(badminton_points / count_badminton)

total_points = volleyball_points + badminton_points + tennis_points
if average_volleyball >= 75 and average_tennis >= 75 and average_badminton >= 75:
    print(f"Congratulations, {name_player}! You won the cruise games with {floor(total_points)} points.")
else:
    print(f"Sorry, {name_player}, you lost. Your points are only {floor(total_points)}.")
