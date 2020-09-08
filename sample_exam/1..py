money_food = float(input())
money_souvenirs = float(input())
money_hotel = float(input())

distance = 210
days = 3
price_fuel = 1.85

hotel_first_day = money_hotel * 0.90
hotel_second_day = money_hotel * 0.85
hotel_third_day = money_hotel * 0.80

first_day = hotel_first_day + money_food + money_souvenirs
second_day = hotel_second_day + money_food + money_souvenirs
third_day = hotel_third_day + money_food + money_souvenirs

fuel_needed = 420/100 * 7
fuel_money = fuel_needed * price_fuel

total_momey = first_day + second_day + third_day + fuel_money

print(f"Money needed: {total_momey:.2f}")