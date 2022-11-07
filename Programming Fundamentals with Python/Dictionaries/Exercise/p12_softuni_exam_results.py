class ExamResults:

    def __init__(self):
        self.student_points = {}
        self.languages = {}

    def max_points(self, student_name, current_points):
        if student_name in self.student_points.keys():
            if current_points >= self.student_points[student_name]:
                self.student_points[student_name] = current_points
        elif student_name not in self.student_points.items():
            self.student_points[student_name] = current_points

    def banned(self, student_name):
        if student_name in self.student_points:
            del self.student_points[student_name]

    def submissions(self, used_language):
        if used_language in self.languages:
            self.languages[used_language] += 1
            return
        self.languages[used_language] = 1


exam = ExamResults()

while True:
    data = input()
    if data == 'exam finished':
        break

    banned_data = data.split('-')

    if banned_data[1] == 'banned':
        exam.banned(banned_data[0])
        continue

    name, language, points = data.split('-')
    points = int(points)

    exam.max_points(name, points)
    exam.submissions(language)

print('Results:')
for student, grade in exam.student_points.items():
    print(student, '|', grade)
print('Submissions:')
for curr_language, submissions in exam.languages.items():
    print(curr_language, '-', submissions)
