transactions_count = int(input())
transactions_made = 0
account_balance = 0

for current_transaction in range(transactions_count):
    transaction_balance = float(input())
    if transaction_balance < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {transaction_balance:.2f}")
    account_balance += transaction_balance

print(f"Total: {account_balance:.2f}")
