# 1. Read input data
width = int(input())
length = int(input())
height = int(input())
volume_home = width * length * height
number_boxes = 0
free_space = volume_home - (number_boxes * 1)
command = ""
done_command = False
while free_space > 0:
    command = input()
    if command != "Done":
        boxes = int(command)
        number_boxes += boxes
        free_space = volume_home - (number_boxes * 1)
    else:
        left_free_space = free_space
        done_command = True
        break

if done_command:
    print(f"{left_free_space} Cubic meters left.")
else:
    needed_space = (number_boxes*1) - volume_home
    print(f"No more free space! You need {needed_space} Cubic meters more.")
