from math import floor
width = float(input())
length = float(input())
height = float(input())
average_height_astrounauts = float(input())

volume_spaceship = width * length * height
volume_room = 2 * 2 * (average_height_astrounauts + 0.40)

how_many_astrounavts = floor(volume_spaceship / volume_room)

if how_many_astrounavts > 10:
    print("The spacecraft is too big.")
elif 3 <= how_many_astrounavts <= 10:
    print(f"The spacecraft holds {how_many_astrounavts} astronauts." )
elif how_many_astrounavts < 3:
    print("The spacecraft is too small.")