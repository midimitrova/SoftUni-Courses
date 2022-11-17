class RageQuit:

    def __init__(self, text):
        self.text = text
        self.new_string = ''
        self.current_string = ''
        self.unique_elements = 0
        self.current_number = ''

    def convert(self):
        index = 0
        while index < len(self.text):
            if not self.text[index].isdigit():
                self.current_string += self.text[index]
                index += 1
            else:
                while self.text[index].isdigit():
                    self.current_number += self.text[index]
                    index += 1
                    if index == len(self.text):
                        break
                self.current_number = int(self.current_number)
                self.new_string += self.current_string.upper() * self.current_number

                self.current_string = ''
                self.current_number = ''

        return self.new_string

    def number_of_unique_elements(self):
        self.unique_elements = len(set(self.new_string))
        return self.unique_elements


data = input()
rage_quit = RageQuit(data)
rage_quit.convert()
rage_quit.number_of_unique_elements()
print(f'Unique symbols used: {rage_quit.unique_elements}\n{rage_quit.new_string}')
