class File:

    def __init__(self, file_name):
        self.file_name = file_name

    def extract(self):
        name_extension = self.file_name[-1]
        name, extension = name_extension.split('.')
        print(f"File name: {name}\nFile extension: {extension}")


file = input().split('\\')
extract_file = File(file)
extract_file.extract()
