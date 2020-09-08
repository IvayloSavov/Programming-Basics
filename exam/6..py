days_tournament = int(input())
money = 0
win = 0
lose = 0

for day in range(1, days_tournament + 1):
    command = input()
    money_day = 0
    win_day = 0
    lose_day = 0
    while command != "Finish":
        sport = str(command)
        win_lose = input()
        if win_lose == "win":
            win_day += 1
            money_day += 20
        elif win_lose == "lose":
            lose_day += 1

        command = input()

    if win_day > lose_day:
        money_day *= 110/100

    money += money_day
    win += win_day
    lose += lose_day

if win > lose:
    money *= 120/100
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")