class Occurrences:

    def __init__(self):
        self.words = {}

    def get_words(self):
        for word in data:
            if word not in self.words.keys():
                self.words[word] = 0
            self.words[word] += 1

    def display(self):
        for key, value in self.words.items():
            if value % 2 != 0:
                print(f'{key}', end=' ')


data = input().lower().split()
odd_occurrence = Occurrences()
odd_occurrence.get_words()
odd_occurrence.display()
