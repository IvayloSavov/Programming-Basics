from sys import maxsize
from math import floor
command = input()
most_powerful_word_points = -maxsize
most_powerful_word = ""
vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
while command != "End of words":
    word = str(command)
    points_current_word = 0
    length_word = len(word)
    for char in word:
        char = ord(char)
        points_current_word += char

    is_vowel = word.startswith(vowels)
    if is_vowel:
        points_current_word *= length_word
        points_current_word = floor(points_current_word)
    else:
        points_current_word /= length_word
        points_current_word = floor(points_current_word)

    if points_current_word >= most_powerful_word_points:
        most_powerful_word_points = points_current_word
        most_powerful_word = word
    command = input()
print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_points}")
