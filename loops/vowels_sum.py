input_text = input()
text_length = len(input_text)
points = 0
for char_pos in range(text_length):
    current_char = input_text[char_pos]
    if current_char == "a":
        points += 1
    if current_char == "e":
        points += 2
    if current_char == "i":
        points += 3
    if current_char == "o":
        points += 4
    if current_char == "u":
        points += 5
print(points)
