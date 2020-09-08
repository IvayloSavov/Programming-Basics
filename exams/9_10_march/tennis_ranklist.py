from math import floor
points_win = 0
win_counter = 0

number_tournaments = int(input())
start_points = int(input())

for tournament in range(1, number_tournaments+1):
    type_tournament = input()
    if type_tournament == "W":
        start_points += 2000
        points_win += 2000
        win_counter += 1
    elif type_tournament == "F":
        start_points += 1200
        points_win += 1200
    elif type_tournament == "SF":
        start_points += 720
        points_win += 720

print(f"Final points: {start_points}")
print(f"Average points: {floor(points_win/number_tournaments)}")
print(f"{win_counter/number_tournaments*100:.2f}%")