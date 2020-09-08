from sys import maxsize
number_bitcoin = int(input())
number_ioan = float(input())
comission = float(input())

ioans_to_dollars = number_ioan * 0.15
dollars_to_bgn = ioans_to_dollars * 1.76

bitcoin_to_bgn = 1168 * number_bitcoin
total = (dollars_to_bgn + bitcoin_to_bgn) / 1.95

comission = total * comission/100

print(f"{total-comission:.2f}")