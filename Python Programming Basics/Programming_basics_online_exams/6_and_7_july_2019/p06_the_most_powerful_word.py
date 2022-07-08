from math import floor

win_word = ''
win_word_points = 0

total_points = 0

word = input()
while word != "End of words":
    for ch in word:
        lenght = len(word)
        ascii_value = ord(ch)
        total_points += ascii_value

    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or\
        word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        total_points *= lenght
    else:
        total_points /= lenght

    if total_points > win_word_points:
        win_word_points = total_points
        win_word = word
        total_points = 0
        curr_points = 0
        word = input()
    else:
        total_points = 0
        curr_points = 0
        word = input()
        continue


print(f"The most powerful word is {win_word} - {floor(win_word_points)}")
