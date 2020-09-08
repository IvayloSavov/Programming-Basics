chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
day = input()
chrysanthemums = 0
roses = 0
tulips = 0


# В празнични дни цените на всички цветя се увеличават с 15%.
# За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Цената за аранжиране на букета винаги е 2лв.

if season == "Spring" or season == "Summer":
    chrysanthemums = (chrysanthemums_count * 2)
    tulips = (tulips_count * 2.5)
    roses = (roses_count * 4.1)
elif season == "Winter" or season == "Autumn":
    chrysanthemums = (chrysanthemums_count * 3.75)
    tulips = (tulips_count * 4.15)
    roses = (roses_count * 4.5)

total = chrysanthemums+roses+tulips

if day == "Y":
    total = total+(total*0.15)

if season == "Spring" and tulips_count > 7:
    total = total-total*0.05
elif season == "Winter" and roses_count >= 10:
    total = total-total*0.1

if chrysanthemums_count+roses_count+tulips_count > 20:
    total = total-total*0.2

total_money = 2+total
print(f'{total_money:.2f}')
