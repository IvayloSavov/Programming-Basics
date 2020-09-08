number_groups = int(input())
total_people = 0
musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0

for group in range(1, number_groups + 1):
    people = int(input())
    total_people += people
    if people <= 5:
        musala_people += people
    elif 6 <= people <= 12:
        monblan_people += people
    elif 13 <= people <= 25:
        kilimandjaro_people += people
    elif 26 <= people <= 40:
        k2_people += people
    elif people >= 41:
        everest_people += people

print(f"{musala_people/total_people * 100:.2f}%")
print(f"{monblan_people/total_people * 100:.2f}%")
print(f"{kilimandjaro_people/total_people * 100:.2f}%")
print(f"{k2_people/total_people * 100:.2f}%")
print(f"{everest_people/total_people * 100:.2f}%")