from sys import maxsize
a = int(input())
b = int(input())
max_passwords = int(input())
combination = 0
max_covered = False

for A in range(35, maxsize):
    if A > 55:
        A = 35
    for B in range(64, maxsize):
        if B > 96:
            B = 64
        for x in range(1, a+1):
            for y in range(1, b+1):
                combination += 1
                print(chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A) + "|", end= "")
                if combination == max_passwords:
                    max_covered = True
                    break
            if max_covered:
                break
        if max_covered:
            break
    if max_covered:
        break