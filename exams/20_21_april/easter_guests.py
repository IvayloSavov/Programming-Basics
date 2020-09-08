from math import floor
# 1. Read input data
income = float(input())
average_grade = float(input())
min_salary = float(input())

excellent_scholarship = False
social_scholarship = False
# 2. Scholarship
# 2.1 social scholarship
if income < min_salary and average_grade > 4.5:
    social_scholarship = True
    social_scholarship = (min_salary * 0.35)
# 2.2 excellent scholarship
if average_grade >= 5.50:
    excellent_scholarship = True
    excellent_scholarship = (average_grade * 25)

if social_scholarship and excellent_scholarship:
    if excellent_scholarship > social_scholarship:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
    elif social_scholarship > excellent_scholarship:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
    elif social_scholarship == excellent_scholarship:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")

elif social_scholarship and excellent_scholarship == False:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif excellent_scholarship and social_scholarship == False:
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")