food_kilograms = int(input())
food_grams = food_kilograms * 1000
eaten_food = 0
command = input()
not_enough = False

while command != "Adopted":
    eaten_food_grams = int(command)
    eaten_food += eaten_food_grams
    command = input()

left_need_food = abs(food_grams - eaten_food)
if food_grams >= eaten_food:
    print(f"Food is enough! Leftovers: {left_need_food} grams.")
else:
    print(f"Food is not enough. You need {left_need_food} grams more.")

