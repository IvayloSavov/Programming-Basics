# 1. Read input data
number_bad_grades = int(input())
count_bad_grade = 0
is_enough = False
count_task = 0
sum_grades = 0
last_task = ""
while count_bad_grade < number_bad_grades:
    name_task = input()
    if name_task != "Enough":
        last_task = name_task
        grade = int(input())
    if name_task == "Enough":
        is_enough = True
        break
    count_task += 1
    sum_grades += grade
    if grade <= 4.00:
        count_bad_grade += 1


if not count_bad_grade < number_bad_grades:
    print(f"You need a break, {count_bad_grade} poor grades.")
elif is_enough:
    average_grade = sum_grades/count_task
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {last_task}")