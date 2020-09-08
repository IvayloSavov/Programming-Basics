weather = input()
temperature = int(input())

if weather == "rain" and temperature < 15:
    print("Take your cold jacket")
elif not weather == "rain" and temperature < 25:
    print("Take your thin jacket")
elif weather == "sun" or temperature > 25:
    print("don't take any jacket")
elif not weather == "rain":
    print("don't take your umbrella")