income = float(input())
number_months_for_saving = int(input())
money_for_month_expenses = float(input())

saving_30_percent = (income * 30/100)
money_left_for_saving_one_month = income - money_for_month_expenses - saving_30_percent

saved_money_for_all_months = number_months_for_saving * money_left_for_saving_one_month

print(f"She can save {money_left_for_saving_one_month/income*100:.2f}%")
print(f"{saved_money_for_all_months:.2f}")
