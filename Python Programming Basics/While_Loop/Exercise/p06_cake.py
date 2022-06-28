cake_width = int(input())
cake_high = int(input())
left_pieces = cake_high * cake_width


command = input()

while command != "STOP":
    pieces = int(command)

    left_pieces -= pieces

    if left_pieces < 0:
        break

    command = input()

if command == "STOP":
    print(f"{left_pieces} pieces are left.")
elif left_pieces < 0:
    print(f"No more cake left! You need {abs(left_pieces)} pieces more.")