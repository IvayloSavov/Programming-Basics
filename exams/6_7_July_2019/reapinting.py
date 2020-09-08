covering_foil  = 1.50
paint = 14.50
razreditel = 5.00
bags = 0.40

# 1. Read input data
need_covering_foil = int(input())
need_paint = int(input())
need_razreditel = int(input())
hours_workers = int(input())

total_paint = need_paint + (need_paint*10/100)
total_covering_foil = need_covering_foil + 2

price_paint = total_paint * paint
price_covering_foil = total_covering_foil * covering_foil
price_razreditel = need_razreditel * razreditel
price_workers = (bags+price_paint+price_covering_foil+price_razreditel) * 30/100 * hours_workers

total = price_paint + price_covering_foil + price_razreditel + price_workers + bags

print(f"Total expenses: {total:.2f} lv.")