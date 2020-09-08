# 1. Read input data
income = float(input())
number_months = int(input())
money_needed = float(input())
# 2. Savings and 30% for unexpected expense
unexpected_expense = income * 0.30
savings = income - money_needed - unexpected_expense
savings_monts = number_months * savings
percent_from_income = (savings / income) * 100

print(f'She can save {percent_from_income:.2f}%')
print(f'{savings_monts:.2f}')