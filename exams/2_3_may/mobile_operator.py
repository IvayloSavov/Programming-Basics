# 1. Read input data
term_contract = input()
type_contract = input()
add_mobile_internet = input()
number_months_pay = int(input())
price = 0
# 2. If term contract and type contract
if term_contract == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == "Middle":
        price = 18.99
    elif type_contract == "Large":
        price = 25.98
    elif type_contract == "ExtraLarge":
        price = 35.99
else:
    if type_contract == "Small":
        price = 8.58
    elif type_contract == "Middle":
        price = 17.09
    elif type_contract == "Large":
        price = 23.59
    elif type_contract == "ExtraLarge":
        price = 31.79
# 3. Tax
tax = price
# 4. If mobile internet
if add_mobile_internet == "yes":
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
# 5. If contract for 2 years
if term_contract == "two":
    discount = tax * 3.75/100
    tax = tax - discount
tax = tax * number_months_pay
# 6. Print
print(f"{tax:.2f} lv.")