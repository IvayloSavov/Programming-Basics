# 1. Read name
name_student = input()
classes = 1
annual_grade = 0
times_failed = 0
is_failed = False
# 2. While grades < 12
while classes <= 12:
    grade = float(input())
    if grade >= 4.00:
        classes += 1
        annual_grade += grade
    else:
        times_failed += 1
        if times_failed == 2:
            is_failed = True
            break
if is_failed:
    print(f"{name_student} has been excluded at {classes} grade")
else:
    average_grade = annual_grade / 12
    print(f"{name_student} graduated. Average grade: {average_grade:.2f}")