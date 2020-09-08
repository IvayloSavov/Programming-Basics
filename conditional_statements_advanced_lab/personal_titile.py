# 1. Read input data
age = float(input())
gender = input().lower()[0]
# first_letter = gender[0]



if gender == 'f':
    if age < 16:
        print("Miss")
    else:
        print("Ms.")
elif gender == 'm':
    if age < 16:
        print("Master")
    else:
        print("Mr.")