n = int(input())

codes = set()

for _ in range(n):
    guest_code = input()

    codes.add(guest_code)

command = input()
while command != 'END':
    if command in codes:
        codes.remove(command)
    command = input()

print(len(codes))
if codes:
    print('\n'.join(sorted(codes)))

