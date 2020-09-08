command = input()
word = ""

while command != "End":
    symbol = str(command)
    word += symbol
    command = input()

print(word + " " + "hey")