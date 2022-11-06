class Phonebook:

    def __init__(self, data):
        self.data = data
        self.phone = ''
        self.name = ''
        self.phonebook_dict = {}
        self.searched_name = ''

    def make_phonebook(self):
        while '-' in self.data:
            self.name, self.phone = self.data.split('-')
            self.phonebook_dict[self.name] = self.phone
            self.data = input()

    def search_contact(self):
        number = int(self.data)
        for _ in range(number):
            self.searched_name = input()
            if self.searched_name in self.phonebook_dict.keys():
                print(f"{self.searched_name} -> {self.phonebook_dict[self.searched_name]}")
            else:
                print(f"Contact {self.searched_name} does not exist.")


command = input()
phonebook = Phonebook(command)
phonebook.make_phonebook()
phonebook.search_contact()

