class Synonym:

    def __init__(self):
        self.words = {}

    def get_words(self):
        for _ in range(number):
            word = input()
            synonym = input()
            if word not in self.words.keys():
                self.words[word] = []
            self.words[word].append(synonym)

    def display(self):
        for key, value in self.words.items():
            print(f'{key} - {", ".join(value)}')


number = int(input())
synonym = Synonym()
synonym.get_words()
synonym.display()
