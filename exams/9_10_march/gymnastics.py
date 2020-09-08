# 1. Read input data
country = input()
instrument = input()
# 2. Grades
if country == "Russia":
    if instrument == "ribbon":
        grade_difficult = 9.100
        grade_performance = 9.400
    elif instrument == "hoop":
        grade_difficult = 9.300
        grade_performance = 9.800
    elif instrument == "rope":
        grade_difficult = 9.600
        grade_performance = 9.000
elif country == "Bulgaria":
    if instrument == "ribbon":
        grade_difficult = 9.600
        grade_performance = 9.400
    elif instrument == "hoop":
        grade_difficult = 9.550
        grade_performance = 9.750
    elif instrument == "rope":
        grade_difficult = 9.500
        grade_performance = 9.400
elif country == "Italy":
    if instrument == "ribbon":
        grade_difficult = 9.200
        grade_performance = 9.500
    elif instrument == "hoop":
        grade_difficult = 9.450
        grade_performance = 9.350
    elif instrument == "rope":
        grade_difficult = 9.700
        grade_performance = 9.150
# 3. Calculate grade
grade = grade_difficult + grade_performance
# 4. Percent
needed = 20 - grade
percent = needed/20 * 100
# 5. Print
print(f"The team of {country} get {grade:.3f} on {instrument}.")
print(f"{percent:.2f}%")
