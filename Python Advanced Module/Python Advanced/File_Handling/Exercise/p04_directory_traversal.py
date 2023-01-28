from os import listdir, path

given_directory = input()


def traverse_dir(current_path, files_by_exc):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element), files_by_exc)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_exc:
                files_by_exc[extension] = []
            files_by_exc[extension].append(element)


files_by_exc = {}
traverse_dir(given_directory, files_by_exc)

with open('ex4_report.txt', 'w') as file:
    for exc, files in sorted(files_by_exc.items()):
        file.write(f'.{exc}\n')
        for file_name in sorted(files):
            file.write(f'--- {file_name}\n')
