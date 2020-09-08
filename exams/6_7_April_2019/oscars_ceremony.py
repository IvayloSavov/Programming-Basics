rent_hall = int(input())

statuetki = 0.70 * rent_hall
food = 0.85 * statuetki
music = food * 1/2

print(f"{rent_hall+statuetki+food+music:.2f}")