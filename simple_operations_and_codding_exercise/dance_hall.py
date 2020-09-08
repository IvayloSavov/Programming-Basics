import math
# 1. Read input data - lenght (L), width (W), side of the wardrobe (A)
L = float(input())
W = float(input())
A = float(input())
# 2. Area of the wardrobe
area_wardrobe = A * A
# 3. Area of the hall
area = L * W
# 4. Area of the bench
area_bench = area / 10
# 5. Space required for 1 dancer
space_1_dancer = 40 + 7000
# 6. Convert space in meters
space = space_1_dancer / 100
# 7. Area hall without wardrobe and bench
area_hall = area - (area_wardrobe + area_bench)
# 8. Calculating how much dancer can use the hall
dancers = area_hall / space
# 9. Convert dancers in centimetres
dancers_1 = dancers * 100
# 10. Printing final results
print(math.floor(dancers_1))