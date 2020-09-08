# 1. Read input data
command = input()
steps_made = 0
going_home = False
steps_made_total = 0
while steps_made_total < 10000:
    if command == "Going home":
        going_home = True
        steps_made_to_home = int(input())
        steps_made_total += steps_made_to_home
        break
    else:
        steps_made = int(command)
        steps_made_total += steps_made
    if steps_made_total >= 10000:
         break
    else:
        command = input()

if steps_made_total >= 10000:
    print(f"Goal reached! Good job!")

elif going_home:
    more_steps = 10000 - steps_made_total
    print(f"{more_steps} more steps to reach goal.")
