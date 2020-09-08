command = input()
tournaments_count = 0
win_count = 0
lose_count = 0
total_matches = 0
while command != "End of tournaments":
    name_tournament = str(command)
    number_matches = int(input())
    total_matches += number_matches
    for match in range (1, number_matches+1):
        points_desi = int(input())
        points_other_team = int(input())
        if points_desi > points_other_team:
            win_count += 1
            print(f"Game {match} of tournament {name_tournament}: win with {points_desi - points_other_team} points.")
        else:
            lose_count += 1
            print(f"Game {match} of tournament {name_tournament}: lost with {points_other_team - points_desi} points.")
    command = input()

print(f"{win_count/total_matches*100:.2f}% matches win")
print(f"{lose_count/total_matches*100:.2f}% matches lost")