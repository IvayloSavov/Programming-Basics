# 1. Read input data
number = int(input())
bonus = 0 #винаги когато ще имаме натрупване трябва да му зададем нулева стойност и не може да се вземе от условната единица, ще работи, но няма да е вярно

if number <= 100:
    bonus = 5
elif number <= 1000:
    bonus = number * 0.2
else:
    bonus = number * 0.1

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

print(bonus)
print(bonus+number)