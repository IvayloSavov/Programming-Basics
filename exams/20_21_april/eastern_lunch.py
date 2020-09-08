# 1. Price of products
price_kozunak = 3.20
price_eggs = 4.35 # za 12 eggs/1 kora
price_kurabia = 5.40 #za kolgram
price_boq_egg = 0.15 #za 1 egg
# 2. Read input data
number_kozunak = int(input())
number_kora_eggs = int(input())
number_kurabia = int(input())
# 3. Prices
kozunak = number_kozunak * price_kozunak
eggs = number_kora_eggs * price_eggs
kurabia = price_kurabia * number_kurabia
boq = number_kora_eggs * price_boq_egg * 12
# 4. Total price
total_price = kozunak + eggs + kurabia + boq
print(f'{total_price:.2f}')



