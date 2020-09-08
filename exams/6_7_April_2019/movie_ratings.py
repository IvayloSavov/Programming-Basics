from sys import maxsize
number_films = int(input())
film_highest_rating = -maxsize
name_film_highest_rating = ""

film_lowest_rating = maxsize
name_film_lowest_rating = ""

count_films = 0
average_rating_film = 0

for film in range(1, number_films + 1):
    name_film = input()
    rating_film = float(input())
    count_films += 1
    average_rating_film += rating_film

    if rating_film > film_highest_rating:
        film_highest_rating = rating_film
        name_film_highest_rating = name_film
    if rating_film < film_lowest_rating:
        film_lowest_rating = rating_film
        name_film_lowest_rating = name_film

average_rating_film /= count_films
print(f"{name_film_highest_rating} is with highest rating: {film_highest_rating:.1f}")
print(f"{name_film_lowest_rating} is with lowest rating: {film_lowest_rating:.1f}")
print(f"Average rating: {average_rating_film:.1f}")