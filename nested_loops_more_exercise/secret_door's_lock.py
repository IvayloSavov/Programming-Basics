max_hundreds = int(input())
max_tens = int(input())
max_units = int(input())

for hundred in range(1, max_hundreds + 1):
    for ten in range(1, max_tens + 1):
        for unit in range(1, max_units + 1):
            if unit % 2 == 0 and hundred % 2 == 0:
                if ten > 1:
                    for i in range(2, ten):
                        if ten % i == 0:
                            break
                    else:
                        print(f"{hundred} {ten} {unit}")