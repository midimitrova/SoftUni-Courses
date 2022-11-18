import re


class VariableNames:

    def __init__(self, text):
        self.text = text

    def find_names(self):
        pattern = r'(?<=\s_)[a-zA-Z]+\b'
        valid_variables = [el.group() for el in re.finditer(pattern, self.text)]
        return ','.join(valid_variables)


data = input()
find_variable = VariableNames(data)
print(find_variable.find_names())
