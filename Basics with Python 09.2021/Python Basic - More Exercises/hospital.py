number_of_days = int(input())

number_of_doctors = 7
number_of_patients = 0
treated_patients = 0
untreated_patients = 0

for day in range(1, number_of_days + 1):
    if day % 3 == 0 and untreated_patients > treated_patients:
        number_of_doctors += 1

    number_of_patients = int(input())

    if number_of_patients <= number_of_doctors:
        treated_patients += number_of_patients

    elif number_of_patients > number_of_doctors:
        treated_patients += number_of_doctors
        untreated_patients += number_of_patients - number_of_doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
