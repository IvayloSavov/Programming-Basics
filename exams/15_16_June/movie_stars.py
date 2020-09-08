budget_actors = float(input())

while budget_actors > 0:
    name_actor = input()
    longer_than_15 = len(name_actor)
    if name_actor == "ACTION":
        break
    elif longer_than_15 > 15:
        remuneration = 0.20 * budget_actors
        budget_actors -= remuneration
    else:
        remuneration = float(input())
        budget_actors -= remuneration

if budget_actors > 0:
    print(f"We are left with {budget_actors:.2f} leva.")
else:
    print(f"We need {abs(budget_actors):.2f} leva for our actors.")

