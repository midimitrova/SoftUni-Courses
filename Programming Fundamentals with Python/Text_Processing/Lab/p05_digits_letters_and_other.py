class DigitsLetters:

    def __init__(self, my_string):
        self.my_string = my_string

    def digits(self):
        are_digits = ''
        for ch in self.my_string:
            if ch.isdigit():
                are_digits += ch
        print(are_digits)

    def letters(self):
        are_letters = ''
        for ch in self.my_string:
            if ch.isalpha():
                are_letters += ch
        print(are_letters)

    def other_characters(self):
        are_others = ''
        for ch in self.my_string:
            if not ch.isalpha() and not ch.isdigit():
                are_others += ch
        print(are_others)


my_string = input()
digit_strings = DigitsLetters(my_string)
digit_strings.digits()
digit_strings.letters()
digit_strings.other_characters()
