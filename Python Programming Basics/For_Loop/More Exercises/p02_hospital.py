days = int(input())

number_doctors = 7
treated_patients = 0
untreated_patients = 0


for day in range(1, days + 1):

    daily_treated = 0
    daily_untreated = 0

    if untreated_patients > treated_patients and day % 3 == 0:
        number_doctors += 1


    number_patients = int(input())

    if number_doctors >= number_patients:
        daily_treated = number_patients
        daily_untreated = 0

    if number_patients > number_doctors:
        daily_untreated = number_patients - number_doctors
        daily_treated = number_patients - daily_untreated



    day += 1


    treated_patients += daily_treated
    untreated_patients += daily_untreated

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")