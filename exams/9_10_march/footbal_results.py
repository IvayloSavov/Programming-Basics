# 1. Read input data
first_match = input()
second_match = input()
third_match = input()
won_games = 0
lost_games = 0
drawn_games = 0
# 2. Read goals
# 2.1 goals first match
home_1 = first_match[0]
guests_1 = first_match[2]
# 2.2 goals second match
home_2 = second_match[0]
guests_2 = second_match[2]
# 2.3 goals third match
home_3 = third_match[0]
guests_3 = third_match[2]
# 3. Checks if
if home_1 > guests_1:
    won_games += 1
elif home_1 == guests_1:
    drawn_games += 1
else:
    lost_games += 1
if home_2 > guests_2:
    won_games += 1
elif home_2 == guests_2:
    drawn_games += 1
else:
    lost_games += 1
if home_3 > guests_3:
    won_games += 1
elif home_3 == guests_3:
    drawn_games += 1
else:
    lost_games += 1
# 4. Print
print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {drawn_games}")
