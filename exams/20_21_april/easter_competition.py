from sys import maxsize
number_breads = int(input())
best_bread_grade = -maxsize
best_beaker = ""

for bread in range(1, number_breads + 1):
    name_baker = input()
    grade_baker = 0
    command = input()
    while command != "Stop":
        grade = int(command)
        grade_baker += grade
        command = input()
        if grade_baker > best_bread_grade:
            best_bread_grade = grade_baker
            best_beaker = name_baker
    print(f"{name_baker} has {grade_baker} points.")
    if best_beaker == name_baker:
        print(f"{best_beaker} is the new number 1!")

print(f"{best_beaker} won competition with {best_bread_grade} points!")