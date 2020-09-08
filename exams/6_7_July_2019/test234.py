command = input()

while command != "End of words":
    word = str(command)
    first_char = word[0]
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    is_vowel = word[0].lower() in vowels
    print()