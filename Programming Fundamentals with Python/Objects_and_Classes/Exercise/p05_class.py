class Class:
    __students__count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.average = 0

    def add_student(self, name: str, grade: float):
        if Class.__students__count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)
            self.average = sum(self.grades) / len(self.students)

    def get_average_grade(self):
        return self.average

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.average:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
