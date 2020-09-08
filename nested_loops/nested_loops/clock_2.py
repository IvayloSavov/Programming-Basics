hours = 0
while hours < 24:
    minutes = 0  # докато тук трябва да ги зануля сам при for цикъл не е нужнно
    while minutes < 60:
        print(f"{hours}:{minutes}")
        minutes += 1

    hours += 1