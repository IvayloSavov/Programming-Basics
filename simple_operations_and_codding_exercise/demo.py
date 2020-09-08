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