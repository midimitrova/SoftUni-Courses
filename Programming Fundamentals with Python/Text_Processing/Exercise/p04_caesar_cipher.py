class Cipher:

    def __init__(self, message):
        self.message = message

    def encrypted_text(self):
        result = ''
        for symbol in self.message:
            result += chr(ord(symbol) + 3)
        return result


text = input()
msg = ''.join(text)
cipher = Cipher(msg)
print(cipher.encrypted_text())
