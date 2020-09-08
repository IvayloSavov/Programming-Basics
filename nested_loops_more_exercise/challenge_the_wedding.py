number_men = int(input())
number_women = int(input())
number_tables = int(input())
count_tables = 0
not_enough_tables = False
for man in range(1, number_men + 1):
    for woman in range(1, number_women + 1):
        count_tables += 1
        if count_tables > number_tables:
            not_enough_tables = True
            break
        else:
            print(f"({man} <-> {woman})", end= " ")
    if not_enough_tables:
        break