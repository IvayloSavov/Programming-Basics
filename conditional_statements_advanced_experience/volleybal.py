from math import floor
# 1. Read input data
type_year = input()
number_holidays_except_weekends = int(input())
number_weekends_to_home_town = int(input())
# 2. Number weekends in Sofia
number_weekends_in_sofia = 48 - number_weekends_to_home_town
# 3. Number weekends play in Sofia
number_weekends_in_sofia_volleyball = number_weekends_in_sofia * 3/4
# 4. Number weekends play holidays
number_holidays_volleyball = number_holidays_except_weekends * 2/3
# 5. Total volleyball
total_volleyball = (number_weekends_to_home_town + number_weekends_in_sofia_volleyball + number_holidays_volleyball)
# 6. If type year
if type_year == "leap":
    bonus_volleyball = total_volleyball * 15/100
    total_volleyball = floor(total_volleyball + bonus_volleyball)
else:
    total_volleyball = floor(number_weekends_to_home_town + number_weekends_in_sofia_volleyball + number_holidays_volleyball)
# 7. Print
print(total_volleyball)


