class Multiplier:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def multiply(self):
        self.first = [ord(num) for num in self.first]
        self.second = [ord(num) for num in self.second]
        first_string_len = len(self.first)
        second_string_len = len(self.second)
        if first_string_len > second_string_len:
            for index in range(first_string_len - second_string_len):
                self.second.append(1)
        elif first_string_len < second_string_len:
            for index in range(second_string_len - first_string_len):
                self.first.append(1)
        print(sum([self.first[index] * self.second[index] for index in range(len(self.first))]))


first_string, second_string = input().split()
multiplier = Multiplier(first_string, second_string)
multiplier.multiply()
