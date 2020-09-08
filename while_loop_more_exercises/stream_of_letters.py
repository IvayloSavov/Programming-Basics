command = input()
word = ""
count_c = 0
count_o = 0
count_n = 0

while command != "End":
    symbol = str(command)
    is_letter = str.isalpha(symbol)
    if is_letter:
        if symbol == "c" or symbol == "o" or symbol == "n":
            if symbol == "c":
                count_c += 1
                if count_c >= 2:
                    word += symbol
            elif symbol == "o":
                count_o += 1
                if count_o >= 2:
                    word += symbol
            elif symbol == "n":
                count_n += 1
                if count_n >= 2:
                    word += symbol
        else:
            word += symbol
    if count_c >= 1 and count_n >= 1 and count_o >= 1:
        print(word, end=" ")
        count_c = 0
        count_o = 0
        count_n = 0
        word = ""

    command = input()