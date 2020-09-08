destination = input()
ani_money = 0
is_going = False
while destination != "End":
    min_budget = float(input())
    while ani_money < min_budget:
        money = float(input())
        ani_money += money
        if ani_money >= min_budget:
            is_going = True
            print(f"Going to {destination}!")
            break
    if is_going:
        ani_money = 0
        is_going = False
        destination = input()


