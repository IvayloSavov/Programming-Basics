from sys import maxsize
number_films = 7
points_favourite_film = -maxsize
name_favourite_film = ""
count_films = 0
for film in range(1, number_films + 1):
    name_film = input()
    points_film = 0
    length_name_film = len(name_film)
    if name_film == "STOP":
        break
    count_films += 1
    for digit in name_film:
        current_char = digit
        is_lower = current_char.islower()
        is_upper = current_char.isupper()
        points_film += ord(current_char)
        if is_lower:
            points_film -= 2 * length_name_film
        elif is_upper:
            points_film -= length_name_film
    if points_film > points_favourite_film:
        points_favourite_film = points_film
        name_favourite_film = name_film

if count_films >= 7:
    print("The limit is reached.")
print(f"The best movie for you is {name_favourite_film} with {points_favourite_film} ASCII sum.")
