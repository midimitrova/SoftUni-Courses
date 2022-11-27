title = input()
content_of_article = input()

comments = []
while True:
    data = input()

    if data == 'end of comments':
        break

    comments.append(data)

print(f'<h1>\n  {title}\n</h1>')
print(f'<article>\n {content_of_article}\n</article>')
for comment in comments:
    print(f'<div>\n   {comment}\n</div>')