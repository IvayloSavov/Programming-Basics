# 1. Read input data
eggs_first_player = int(input())
eggs_second_player = int(input())

n = eggs_first_player + eggs_second_player

for round in range(n):
    winner = input()
    if winner == "one":
        eggs_second_player -= 1
    elif winner == "two":
        eggs_first_player -= 1

    if eggs_first_player <= 0:
        break
    elif eggs_second_player <= 0:
        break

    if winner == "End of battle":
        break

if eggs_first_player <= 0:
    print(f"Player one is out of eggs. Player two has {eggs_second_player} eggs left.")
elif eggs_second_player <= 0:
    print(f"Player two is out of eggs. Player one has {eggs_first_player} eggs left.")
elif winner == "End of battle":
    print(f"Player one has {eggs_first_player} eggs left.\nPlayer two has {eggs_second_player} eggs left.")
