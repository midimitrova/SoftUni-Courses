class StudentAcademy:

    def __init__(self):
        self.student_grades = {}
        self.average_grades = {}

    def get_student_name_and_grade(self, name: str, grade: float):
        if name not in self.student_grades:
            self.student_grades[name] = []
            self.student_grades[name].append(grade)
        else:
            self.student_grades[name].append(grade)

    def get_average_grade(self):
        for name, grade in self.student_grades.items():
            average_grade = sum(self.student_grades[name]) / len(self.student_grades[name])
            if average_grade >= 4.50:
                self.average_grades[name] = average_grade

    def __repr__(self):
        result = ''
        for name, averageGrade in self.average_grades.items():
            result += f"{name} -> {self.average_grades[name]:.2f}\n"
        return result


academy = StudentAcademy()
number = int(input())

for _ in range(number):
    name = input()
    grade = float(input())
    academy.get_student_name_and_grade(name, grade)

academy.get_average_grade()
print(academy)
