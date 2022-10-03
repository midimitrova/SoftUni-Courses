first_line = input().split()
second_line = input().split()
third_line = input().split()

first_player = '1'
second_player = '2'

while True:
    if ((first_line[0] == '1' and first_line[1] == '1' and first_line[2] == '1') or
            (second_line[0] == '1' and second_line[1] == '1' and second_line[2] == '1') or
            (third_line[0] == '1' and third_line[1] == '1' and third_line[2] == '1') or
            (first_line[0] == '1' and second_line[0] == '1' and third_line[0] == '1') or
            (first_line[1] == '1' and second_line[1] == '1' and third_line[1] == '1') or
            (first_line[2] == '1' and second_line[2] == '1' and third_line[2] == '1') or
            (first_line[0] == '1' and second_line[1] == '1' and third_line[2] == '1') or
            (first_line[2] == '1' and second_line[1] == '1' and third_line[0] == '1')):
        print("First player won")
        break
    elif ((first_line[0] == '2' and first_line[1] == '2' and first_line[2] == '2') or
          (second_line[0] == '2' and second_line[1] == '2' and second_line[2] == '2') or
          (third_line[0] == '2' and third_line[1] == '2' and third_line[2] == '2') or
          (first_line[0] == '2' and second_line[0] == '2' and third_line[0] == '2') or
          (first_line[1] == '2' and second_line[1] == '2' and third_line[1] == '2') or
          (first_line[2] == '2' and second_line[2] == '2' and third_line[2] == '2') or
          (first_line[0] == '2' and second_line[1] == '2' and third_line[2] == '2') or
          (first_line[2] == '2' and second_line[1] == '2' and third_line[0] == '2')):
        print("Second player won")
        break
    else:
        print('Draw!')
        break
