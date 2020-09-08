counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein_shake = 0
counter_protein_bar = 0
counter_training = 0
counter_protein = 0

number_clients = int(input())
for client in range(1, number_clients+1):
    activity = input()
    if activity == "Back":
        counter_back += 1
        counter_training += 1
    elif activity == "Chest":
        counter_chest += 1
        counter_training += 1
    elif activity == "Legs":
        counter_legs += 1
        counter_training += 1
    elif activity == "Abs":
        counter_abs += 1
        counter_training += 1
    elif activity == "Protein shake":
        counter_protein_shake += 1
        counter_protein += 1
    elif activity == "Protein bar":
        counter_protein_bar += 1
        counter_protein += 1

total = counter_training + counter_protein

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_protein_shake} - protein shake")
print(f"{counter_protein_bar} - protein bar")
print(f"{counter_training/total*100:.2f}% - work out")
print(f"{counter_protein/total*100:.2f}% - protein")