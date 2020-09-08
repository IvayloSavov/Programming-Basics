control_number = int(input())
count = 0
password = ""
is_found = False
for a in range(1, 9+1):
    for b in range(1, 9+1):
        for c in range(1, 9+1):
            for d in range(1, 9+1):
                if a < b and c > d and a*b + c*d == control_number :
                    print(f"{a}{b}{c}{d}", end= " ")
                    count += 1
                    if count == 4:
                        password = (str(a) + str(b) + str(c) + str(d))
                        is_found = True
print()
if is_found:
    print(f"Password: {password}")
else:
    print("No!")
