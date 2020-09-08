# 1. Read input data the square meters for greening
square_meters_for_greening = float(input())
# 2. Price for one square meter
price_for_one_square_meter = 7.61
# 3. Calculate the price
price = (square_meters_for_greening * price_for_one_square_meter)
# 4. Calculate the discount
discount = (price * 0.18)
# 5. Calculate the final price
final_price = (price - discount)
# 6. Print the final price
print(f'The final price is: {final_price:.2f} lv.')
# 7. Print the discount
print(f'The discount is: {discount:.2f} lv.')