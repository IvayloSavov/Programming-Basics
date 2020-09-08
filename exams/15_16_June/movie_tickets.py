
a1 = int(input())
a2 = int(input())
n = int(input())
a2_1 = a2-1

for symbol_1 in range(a1, a2_1):
    for symbol_2 in range(1, n-1):
        for symbol_3 in range(1, 1):
            for symbol_4 in range(symbol_1):
                ticket = f"{chr(symbol_1)}-{symbol_2}{symbol_3}{chr(symbol_4)}"
                if symbol_1 % 2 == 1 and (symbol_2 + symbol_3 + symbol_4) % 2 == 1:
                    print(ticket)
