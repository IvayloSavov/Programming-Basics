number_days = int(input())
doctors = 7
accepted_patients = 0
rejected_patients = 0

for day in range(1, number_days + 1):
    if day % 3 == 0 and rejected_patients > accepted_patients:
        doctors += 1
    patient_per_day = int(input())
    if patient_per_day >= doctors:
        accepted_patients += doctors
        rejected_patients += (patient_per_day - doctors)
    elif patient_per_day <= doctors:
        accepted_patients += patient_per_day

print(f"Treated patients: {accepted_patients}.")
print(f"Untreated patients: {rejected_patients}.")