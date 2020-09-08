packet_pens = 5.80
packet_markers = 7.20
fluid = 1.20

number_pens = int(input())
number_markers = int(input())
number_fluid = float(input())
percent_discount = int(input())

total = ((number_pens*packet_pens) + (number_markers*packet_markers) + (fluid * number_fluid))
discount = total * percent_discount/100
total -= discount

print(f"{total:.3f}")