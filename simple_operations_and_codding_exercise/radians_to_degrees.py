# 1. We are importing math library
from math import pi
# 2. Read input data for radians
rad = float(input())
# 3. Converting radians to degrees and rounding
degrees = round(rad * 180/pi)
# 4. Printing
print(degrees)