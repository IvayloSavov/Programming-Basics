# 1. Read input data
number_open_tabs = int(input())
salary = int(input())


for tabs in range (number_open_tabs):
    web_side_name = str(input())
    if web_side_name == "Facebook":
        salary -= 150
    elif web_side_name == "Instagram":
        salary -= 100
    elif web_side_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)



