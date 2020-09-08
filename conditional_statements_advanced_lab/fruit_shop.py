fruit = input()
day_of_week = input()
quanity = float(input())

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday":
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.20
    else:
        print("error")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
else:
    print("error")

else:
    print("error")

print(price)
