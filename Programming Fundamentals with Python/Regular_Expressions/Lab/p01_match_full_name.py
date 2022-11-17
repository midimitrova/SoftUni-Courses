import re


class MatchFullName:

    def __init__(self, names):
        self.names = names

    def match_name(self):
        pattern = r"\b[A-Z][a-z]+\b [A-Z][a-z]+\b"
        searched_names = re.findall(pattern, self.names)
        return ' '.join(searched_names)


names = input()
match_names = MatchFullName(names)
print(match_names.match_name())
