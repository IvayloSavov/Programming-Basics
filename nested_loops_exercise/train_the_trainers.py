judge_people = int(input())
name_presentation = input()
average_grade_student = 0
average_grade_total = 0
grade_total = 0
grade_sum_student = 0
count_grade_total = 0
count_grade_student = 0

while name_presentation != "Finish":
    for grades in range(1, judge_people + 1):
        grade = float(input())
        grade_sum_student += grade
        grade_total += grade
        count_grade_student += 1
        count_grade_total += 1

    average_grade_student = grade_sum_student / count_grade_student
    print(f"{name_presentation} - {average_grade_student:.2f}.")
    grade_sum_student = 0
    average_grade_student = 0
    count_grade_student = 0
    name_presentation = input()

if name_presentation == "Finish":
    average_grade_total = grade_total / count_grade_total
    print(f"Student's final assessment is {average_grade_total:.2f}." )