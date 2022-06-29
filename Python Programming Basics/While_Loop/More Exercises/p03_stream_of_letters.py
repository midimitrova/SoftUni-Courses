letter = ''
text_entry = ''
con_list = ''
secret_world = ''

while letter != "End":
    letter = input()
    if letter.isalpha():
        if letter in 'con':
            if letter in con_list:
                text_entry += letter
            else:
                con_list += letter
                if ('c' in con_list) and ('o' in con_list) and ('n' in con_list):
                    text_entry += ' '
                    con_list = ''
                    secret_world = text_entry
        else:
            if letter != "End":
                text_entry += letter

print(secret_world)

