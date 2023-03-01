class vowels:
    ALL_VOWELS = 'aeiuyo'

    def __init__(self, text):
        self.text = text
        self.idx_chr = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.idx_chr > len(self.text) - 1:
                raise StopIteration

            if self.text[self.idx_chr].lower() not in vowels.ALL_VOWELS:
                self.idx_chr += 1
                continue

            result = self.text[self.idx_chr]
            self.idx_chr += 1
            return result


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
