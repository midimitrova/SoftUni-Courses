fav_book = input()
book_cnt = 0
book = input()

while fav_book != "No More Books":

    if book == fav_book:
        print(f"You checked {book_cnt} books and found it.")
        break

    if book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_cnt} books.")
        break

    book_cnt += 1
    book = input()



