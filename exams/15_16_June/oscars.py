name_actor = input()
points_academy = float(input())
number_judges = int(input())
is_nominated = False

for judge in range (1, number_judges + 1):
    name_judge = input()
    point_judge = float(input())
    length_name_judge = len(name_judge)

    points_actors = length_name_judge * point_judge / 2
    points_academy += points_actors
    if points_academy > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_academy:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {1250.5 - points_academy:.1f} more!")