country = input()
device = input()

grade_difficulty = 0
grade_performance = 0
max_grade = 20

if country == "Russia":
    if device == "ribbon":
        grade_difficulty = 9.100
        grade_performance = 9.400
    elif device == "hoop":
        grade_difficulty = 9.300
        grade_performance = 9.800
    elif device == "rope":
        grade_difficulty = 9.600
        grade_performance = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        grade_difficulty = 9.600
        grade_performance = 9.400
    elif device == "hoop":
        grade_difficulty = 9.550
        grade_performance = 9.750
    elif device == "rope":
        grade_difficulty = 9.500
        grade_performance = 9.400
elif country == "Italy":
    if device == "ribbon":
        grade_difficulty = 9.200
        grade_performance = 9.500
    elif device == "hoop":
        grade_difficulty = 9.450
        grade_performance = 9.350
    elif device == "rope":
        grade_difficulty = 9.700
        grade_performance = 9.150

total_grade = grade_difficulty + grade_performance
percentage = ((max_grade - total_grade) / max_grade) * 100
print(f"The team of {country} get {total_grade:.3f} on {device}.")
print(f"{percentage:.2f}%")