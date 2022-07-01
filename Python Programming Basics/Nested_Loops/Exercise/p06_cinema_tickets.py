cnt_student = 0
cnt_standard = 0
cnt_kid = 0
total_tickets = 0
curr_tickets = 0

movie = input()
while movie != "Finish":
    free_places = int(input())
    while free_places > 0:

        ticket = input()

        if ticket == "student":
            cnt_student += 1
            total_tickets += 1
            curr_tickets += 1
        elif ticket == "standard":
            cnt_standard += 1
            total_tickets += 1
            curr_tickets += 1
        elif ticket == "kid":
            cnt_kid += 1
            total_tickets += 1
            curr_tickets += 1

        if ticket == "End":
            print(f"{movie} - {(curr_tickets / free_places) * 100:.2f}% full.")
            break

        if curr_tickets >= free_places:
            print(f"{movie} - {(curr_tickets / free_places) * 100:.2f}% full.")
            break

    curr_tickets = 0
    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{(cnt_student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(cnt_standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(cnt_kid / total_tickets) * 100:.2f}% kids tickets.")









