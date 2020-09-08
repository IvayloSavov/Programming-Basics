from sys import maxsize
number_students = int(input())
count_2_299 = 0
count_3_399 = 0
count_4_499 = 0
count_5_and_more = 0
average_grade_exam = 0

for student in range(1, number_students + 1):
    grade_student = float(input())
    average_grade_exam += grade_student
    if 2.00 <= grade_student <= 2.99:
        count_2_299 += 1
    if 3.00 <= grade_student <= 3.99:
        count_3_399 += 1
    if 4.00 <= grade_student <= 4.99:
        count_4_499 += 1
    if 5.00 <= grade_student <= maxsize:
        count_5_and_more += 1

print(f"Top students: {count_5_and_more/number_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {count_4_499/number_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {count_3_399/number_students * 100:.2f}%")
print(f"Fail: {count_2_299/number_students * 100:.2f}%")
print(f"Average: {average_grade_exam/number_students:.2f}")

