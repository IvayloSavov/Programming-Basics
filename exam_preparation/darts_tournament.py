start_points = int(input())
is_win = False
shoots = 0
is_win_bullseye = False

while start_points > 0:
    sector = input()
    shoots += 1
    if sector == "bullseye":
        is_win_bullseye = True
        break
    else:
        number_points = int(input())

    if sector == "number section":
        number_points = number_points
        start_points -= number_points
    elif sector == "double ring":
        number_points *= 2
        start_points -= number_points
    elif sector == "triple ring":
        number_points *= 3
        start_points -= number_points
    if sector == "bullseye":
        is_win_bullseye = True
        break
    if start_points == 0:
        is_win = True
        break


if is_win:
    print(f"Congratulations! You won the game in {shoots} moves!")
elif is_win_bullseye:
    print(f"Congratulations! You won the game with a bullseye in {shoots} moves!")
else:
    print(f"Sorry, you lost. Score difference: {abs(start_points)}.")