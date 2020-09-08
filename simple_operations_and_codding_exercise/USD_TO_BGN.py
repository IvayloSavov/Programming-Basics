# 1. Read input data for the USD
USD = float(input())
# 2. Exchange rate
exchange_rate = 1.79549
# 3. Converting USD to BGN
converting = USD * exchange_rate
# 4. Rounding the converting
rounding = round(converting, 2)
# 5. Print
print(rounding)