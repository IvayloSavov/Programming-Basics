number_days = int(input())
food = float(input())

cookies = 0
eaten_food = 0
eaten_food_dog = 0
eaten_food_cat = 0

for day in range(1, number_days + 1):
    food_dog = int(input())
    eaten_food_dog += food_dog
    food_cat = int(input())
    eaten_food_cat += food_cat
    eaten_food_day = food_dog + food_cat
    eaten_food += eaten_food_day
    if day % 3 == 0:
        cookies_day = eaten_food_day * 10/100
        cookies += cookies_day

print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{eaten_food/food * 100:.2f}% of the food has been eaten.")
print(f"{eaten_food_dog/eaten_food*100:.2f}% eaten from the dog.")
print(f"{eaten_food_cat/eaten_food*100:.2f}% eaten from the cat.")