version = input().split('.')
version = int(''.join(version))
current_version = version + 1
output_version = '.'.join(str(current_version))
print(output_version)


