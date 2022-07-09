movie = input()
student_cnt = 0
standard_cnt = 0
kid_cnt = 0
curr_tickets = 0
total_tickets = 0


while movie != "Finish":
    free_places = int(input())

    type_ticket = input()

    while type_ticket != "End":
        if type_ticket == "student":
            student_cnt += 1
            curr_tickets += 1
        elif type_ticket == "standard":
            standard_cnt += 1
            curr_tickets += 1
        elif type_ticket == "kid":
            kid_cnt += 1
            curr_tickets += 1

        if curr_tickets >= free_places:
            break

        type_ticket = input()

    print(f"{movie} - {(curr_tickets / free_places) * 100:.2f}% full.")
    # student_cnt = 0
    # standard_cnt = 0
    # kid_cnt = 0
    total_tickets += curr_tickets
    curr_tickets = 0
    movie = input()

if movie == "Finish":
    print(f"Total tickets: {total_tickets}")
    print(f"{(student_cnt / total_tickets) * 100:.2f}% student tickets.")
    print(f"{(standard_cnt / total_tickets) * 100:.2f}% standard tickets.")
    print(f"{(kid_cnt / total_tickets) * 100:.2f}% kids tickets.")

