number_games_sold = int(input())

count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0

for game in range(1, number_games_sold + 1):
    name_game = input()
    if name_game == "Hearthstone":
        count_hearthstone += 1
    elif name_game == "Fornite":
        count_fornite += 1
    elif name_game == "Overwatch":
        count_overwatch += 1
    else:
        count_others += 1

print(f"Hearthstone - {count_hearthstone/number_games_sold*100:.2f}%\nFornite - {count_fornite/number_games_sold*100:.2f}%\nOverwatch - {count_overwatch/number_games_sold*100:.2f}%\nOthers - {count_others/number_games_sold*100:.2f}%")