class Ranking:

    def __init__(self):
        self.data_contest = {}
        self.user_dictionary = {}

    def collect_information_contest(self, contest: str, password: str):
        self.data_contest[contest] = password

    def submissions(self, student_contest: str, student_password: str, name: str, points: int):
        if student_contest in self.data_contest.keys() and student_password in self.data_contest.values():
            if name not in self.user_dictionary.keys():
                self.user_dictionary[name] = {student_contest: points}
            elif student_contest not in self.user_dictionary[name]:
                self.user_dictionary[name][student_contest] = points
            elif student_contest in self.user_dictionary[name]:
                if points >= self.user_dictionary[name][student_contest]:
                    self.user_dictionary[name][student_contest] = points

    def max_points(self):
        list_values = {}
        for name, value in self.user_dictionary.items():
            list_values[name] = sum(value.values())
        best_candidate = max(list_values, key=list_values.get)
        total_score = max(list_values.values())
        print(f"Best candidate is {best_candidate} with total {total_score} points.")

    def show_ranking_results(self):
        ordered_dictionary = dict(sorted(self.user_dictionary.items()))
        print('Ranking:')
        for username, contest in ordered_dictionary.items():
            print(username)
            values_dict = dict(sorted(contest.items(), key=lambda item: -item[1]))
            for key, value in values_dict.items():
                print('# ', key, '->', value)


ranking = Ranking()
while True:
    data = input()
    if data == 'end of contests':
        break
    contest, password = data.split(':')
    ranking.collect_information_contest(contest, password)

while True:
    command = input()
    if command == 'end of submissions':
        break
    student_contest, student_password, name, points = command.split('=>')
    points = int(points)
    ranking.submissions(student_contest, student_password, name, points)

ranking.max_points()
ranking.show_ranking_results()
