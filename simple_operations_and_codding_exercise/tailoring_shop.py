# 1. Read input data
number_of_tables = int(input())
lenght_of_tables = float(input())
width_of_tables = float(input())
# 2. Price for 1 square meter in UDS
price_tablecloth_for_1_square_meter = 7
price_quads_for_1_square_meter = 9
# 3. Lenght and width for tablecloths after extra fabric
lenght_tabclecloth = lenght_of_tables + 2 * 0.3
width_tablecloth = width_of_tables + 2 * 0.3
# 4. Lenght and width for quads
lenght_quads = lenght_of_tables / 2
# 5. Calculating the needed fabric (square are of tablecloth and quads)
fabric_tablecloth = (lenght_tabclecloth * width_tablecloth) * number_of_tables
fabric_quads = (lenght_quads * lenght_quads) * number_of_tables
# 6. Calculating the price in USD
price_tablecloth = fabric_tablecloth * price_tablecloth_for_1_square_meter
price_quads = fabric_quads * price_quads_for_1_square_meter
# 7. Total price in dolars
price_in_dolars = (price_tablecloth + price_quads)
# 8. Exchange rate for USD to BGN
exchange_rate = 1.85
# 9. Converting USD to BGN
price_in_leva = price_in_dolars * exchange_rate
# . Print final price and formating
print(f'{price_in_dolars:.2f} USD')
print(f'{price_in_leva:.2f} BGN')