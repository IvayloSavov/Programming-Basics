# 1. Read input data
number_days = int(input())
number_confectioner = int(input())
number_cakes = int(input())
number_corrugurations = int(input())
number_pancakes = int(input())
# 2. Prices
price_cake = 45
price_corruguration = 5.80
price_pancake = 3.20
# 3. Prices for each product
cake = number_cakes * price_cake
corruguration = number_corrugurations * price_corruguration
pancakes = number_pancakes * price_pancake
# 4. Total price for one day
total_price = (cake + corruguration + pancakes) * number_confectioner
# 5. Price for the all days
final_price = total_price * number_days
# 6. Expenses
expences = final_price * (1/8)
# 7. Final money
final_money = final_price - expences
# 8. Print
print(f'{final_money:.2f}')
