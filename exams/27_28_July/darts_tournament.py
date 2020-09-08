start_points = int(input())
is_bullseye = False
is_win = False
number_shoots = 0
while start_points > 0:
    sector = input()
    number_shoots += 1
    if sector == "bullseye":
        is_bullseye = True
        break
    else:
        number_points = int(input())

    if sector == "number section":
        start_points -= number_points
    elif sector == "double ring":
        number_points *= 2
        start_points -= number_points
    elif sector == "triple ring":
        number_points *= 3
        start_points -= number_points
    if sector == "bullseye":
        is_bullseye = True
        break
    if start_points == 0:
        is_win = True
        break

if is_win:
    print(f"Congratulations! You won the game in {number_shoots} moves!")
elif is_bullseye:
    print(f"Congratulations! You won the game with a bullseye in {number_shoots} moves!")
elif start_points < 0:
    print(f"Sorry, you lost. Score difference: {abs(start_points)}.")