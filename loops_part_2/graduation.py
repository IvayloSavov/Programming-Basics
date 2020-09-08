# 1. Read name
name_student = input()
classes = 1
annual_grade = 0
# 2. While grades < 12
while classes <= 12:
    grade = float(input())
    if grade >= 4.00:
        classes += 1
        annual_grade += grade
    else:
        while grade >= 4.00:
            grade = float(input())

average_grade = annual_grade / 12
print(f"{name_student} graduated. Average grade: {average_grade:.2f}")