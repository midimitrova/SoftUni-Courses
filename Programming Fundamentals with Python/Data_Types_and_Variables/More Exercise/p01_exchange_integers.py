a = int(input())
b = int(input())

c = a

print(f'Before:\na = {a}\nb = {b}')

a = b
b = c

print(f'After:\na = {a}\nb = {b}')