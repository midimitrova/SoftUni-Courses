class Course:

    def __init__(self):
        self.courses = {}

    def register(self, course_name: str, student_name: str):
        if course_name not in self.courses:
            self.courses[course_name] = []
            self.courses[course_name].append(student_name)
        else:
            self.courses[course_name].append(student_name)


course = Course()
data = input()
while data != 'end':
    course_name, name = data.split(' : ')
    course.register(course_name, name)
    data = input()

for course_name, registered_students in course.courses.items():
    print(f"{course_name}: {len(course.courses[course_name])}")
    for name in course.courses[course_name]:
        print(f"-- {name}")
