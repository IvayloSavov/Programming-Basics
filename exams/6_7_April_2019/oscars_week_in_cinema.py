name_film = input()
type_hall = input()
number_tickets = int(input())
price = 0

if type_hall == "normal":
    if name_film == "A Star Is Born":
        price = 7.50
    elif name_film == "Bohemian Rhapsody":
        price = 7.35
    elif name_film == "Green Book":
        price = 8.15
    elif name_film == "The Favourite":
        price = 8.75

elif type_hall == "luxury":
    if name_film == "A Star Is Born":
        price = 10.50
    elif name_film == "Bohemian Rhapsody":
        price = 9.45
    elif name_film == "Green Book":
        price = 10.25
    elif name_film == "The Favourite":
        price = 11.55

elif type_hall == "ultra luxury":
    if name_film == "A Star Is Born":
        price = 13.50
    elif name_film == "Bohemian Rhapsody":
        price = 12.75
    elif name_film == "Green Book":
        price = 13.25
    elif name_film == "The Favourite":
        price = 13.95

total_money = price * number_tickets

print(f"{name_film} -> {total_money:.2f} lv.")