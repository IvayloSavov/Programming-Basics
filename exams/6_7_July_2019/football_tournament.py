name_team = input()
number_games = int(input())
points = 0
w_count = 0
d_count = 0
l_count = 0

for game in range(1, number_games + 1):
    result_game = input()
    if result_game == "W":
        points += 3
        w_count += 1
    elif result_game == "D":
        points += 1
        d_count += 1
    elif result_game == "L":
        l_count += 1

if number_games == 0:
    print(f"{name_team} hasn't played any games during this season.")
else:
    total = w_count + d_count + l_count
    win_rate = w_count / total * 100
    print(f"{name_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_count}")
    print(f"## D: {d_count}")
    print(f"## L: {l_count}")
    print(f"Win rate: {win_rate:.2f}%")
