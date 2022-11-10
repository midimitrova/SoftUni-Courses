class Usernames:

    def __init__(self, users):
        self.users = users

    def valid_username(self, username: str):
        allowed_symbols = ['_', '-']
        if 3 <= len(username) <= 16:
            for character in username:
                if character.isalnum() or character in allowed_symbols:
                    continue
                return
        else:
            return
        print(username)


list_usernames = input().split(', ')
username = Usernames(list_usernames)
while len(list_usernames):
    name = list_usernames[0]
    username.valid_username(name)
    list_usernames.pop(0)


