# 1. Read input data
N1 = int(input())
N2 = int(input())
operator = input()
function = 0
# 2. Function
if operator == "+":
    function = N1 + N2
    if function % 2 == 0:
        print(f"{N1} {operator} {N2} = {function} - even")
    else:
        print(f"{N1} {operator} {N2} = {function} - odd")
elif operator == "-":
    function = N1 - N2
    if function % 2 == 0:
        print(f"{N1} {operator} {N2} = {function} - even")
    else:
        print(f"{N1} {operator} {N2} = {function} - odd")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        function = N1 / N2
        print(f"{N1} / {N2} = {function:.2f}")
elif operator == "*":
    function = N1 * N2
    if function % 2 == 0:
        print(f"{N1} {operator} {N2} = {function} - even")
    else:
        print(f"{N1} {operator} {N2} = {function} - odd")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        function = N1 % N2
        print(f"{N1} % {N2} = {function}")
