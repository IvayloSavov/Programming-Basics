input_text = input()
text_length = len(input_text)
points = 0
for index, char in enumerate(input_text): #тук няма да имаме нужда от проверка на текущия символ, тъй като цикълът ще го приема като стринг, а не като число
    if char == "a":
        points += 1
    if char == "e":
        points += 2
    if char == "i":
        points += 3
    if char == "o":
        points += 4
    if char == "u":
        points += 5
print(points)
print(index)