# 2. convert data to the correct type
number_of_dogs = int(input())
number_of_animals = int(input())
# 3. Calculate money needed for dog food
price_for_dogs = number_of_dogs * 2.50
# 4. Calculate money needed for other animals food
price_for_animals = number_of_animals * 4
# 5. Calculate total
(total_cost) = price_for_dogs + price_for_animals
# 6. Print and format
print(f'{total_cost:.2f} lv.')