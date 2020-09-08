from math import floor
# 1. Read input data
income = float(input())
average_result = float(input())
minimum_salary = float(input())

excellent_scholarship = 0
social_scholarship = 0

# 2. Social or excellent scholarship
# 2.1. excellent scholarship
if income < minimum_salary and average_result > 4.5:
    social_sholarship = floor((minimum_salary * 0.35))
if average_result >= 5.50:
    excellent_scholarship = floor(average_result * 25)

# 3. Which one scholarship

if income < minimum_salary and average_result > 4.5 and average_result >= 5.50:
        if social_sholarship < excellent_scholarship:
            print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
        elif social_sholarship > excellent_scholarship:
            print(f'You get a Social scholarship {social_sholarship} BGN')
        elif social_scholarship == excellent_scholarship:
            print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')

elif not income < minimum_salary and average_result > 4.5 and average_result >= 5.50:
    if social_scholarship > 0  and excellent_scholarship == 0:
        print(f'You get a Social scholarship {social_sholarship} BGN')
    elif excellent_scholarship > 0 and social_scholarship == 0:
        print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')

else:
    print('You cannot get a scholarship!')