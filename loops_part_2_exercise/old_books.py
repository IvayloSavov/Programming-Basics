searched_book = input()
capacity_library = int(input())
book = input()
count = 0
no_more_book = False
while book != searched_book:
    count += 1
    if count >= capacity_library:
        no_more_book = True
        break
    book = input()

if book == searched_book:
    print(f"You checked {count} books and found it.")
elif no_more_book:
    print("The book you search is not here!")
    print(f"You checked {count} books.")