name_player = input()
start_points = 301
command = input()
leg_win = False
is_fail = False
success_shots = 0
fail_shots = 0
while command != "Retire":
    field = str(command)
    points = int(input())
    if points > start_points:
        is_fail = True
        fail_shots += 1
    if not is_fail:
        if field == "Single":
            single_points = points * 1
            start_points -= points
            success_shots += 1
        elif field == "Double":
            double_points = points * 2
            if double_points > start_points:
                is_fail = True
                fail_shots += 1
            else:
                start_points = start_points - (points * 2)
                success_shots += 1
        elif field == "Triple":
            triple_points = points * 3
            if triple_points > start_points:
                is_fail = True
                fail_shots += 1
            else:
                start_points = start_points - (points * 3)
                success_shots += 1
    is_fail = False
    if start_points == 0:
        leg_win = True
        break
    else:
        command = input()

if leg_win:
    print(f"{name_player} won the leg with {success_shots} shots.")
elif command == "Retire":
    print(f"{name_player} retired after {fail_shots} unsuccessful shots.")
