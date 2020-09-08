# 1. Read input data
price_brashno = float(input())
kg_brashno = float(input())
kg_sugar = float(input())
number_kora_eggs = int(input())
number_maq = int(input())
# 2. Price
price_sugar = price_brashno - (price_brashno * 0.25)
price_eggs = price_brashno + (price_brashno * 0.1)
price_maq = price_sugar - (price_sugar * 0.8)
# 3. Money
money_brashno = price_brashno * kg_brashno
money_sugar = price_sugar * kg_sugar
money_eggs = price_eggs * number_kora_eggs
money_maq = number_maq * price_maq
# 4. Total
total = money_brashno + money_sugar + money_eggs + money_maq
# 5. Print
print(f'{total:.2f}')


