class Students:
    def __init__(self, data):
        self.name = ''
        self.id = ''
        self.course_name = ''
        self.courses = {}
        self.data = data

    def get_information(self):
        while ':' in self.data:
            self.name, self.id, self.course_name = self.data.split(':')

            if self.course_name not in self.courses.keys():
                self.courses[self.course_name] = {}
            self.courses[self.course_name][self.id] = self.name
            self.data = input()

    def searched_course(self):
        searched_course = self.data
        searched_course_as_list = searched_course.split('_')
        searched_course = ' '.join(searched_course_as_list)
        return searched_course

    def display(self):
        for course_info in self.courses.keys():
            if course_info == self.searched_course():
                for id, name in self.courses[course_info].items():
                    print(f"{name} - {id}")


command = input()
student = Students(command)
student.get_information()
student.searched_course()
student.display()
