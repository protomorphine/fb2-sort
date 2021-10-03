import os
from bs4 import BeautifulSoup

print('Укажите папку с неотсортированными книгами')
print('ВНИМАНИЕ! После имени папки необходимо обязательно добавить / в конце')
print('Например: library/')
LIBRARY = input('> ') # папка с .fb2 файлами, / в конце обязателен!

files = os.listdir(LIBRARY)
print("Рабочая папка: " + LIBRARY)

for file in files:
    try:
        book = open(LIBRARY + file, encoding='utf-8').read()
    except UnicodeDecodeError:
        book = open(LIBRARY + file).read()
    except PermissionError:
        continue

    soup = BeautifulSoup(book, features="html.parser")

    author = ''

    for name in soup.find('author'):
        if len(name.text) <= 15:
            author += name.text + ' '

    author = author.strip()

    book_title = soup.find('book-title').text + '.fb2'
    os.rename(LIBRARY + file, LIBRARY + book_title)

    dest_path = LIBRARY + author + '/' + book_title
    if not os.path.exists(LIBRARY + author):
        os.mkdir(LIBRARY + author)

    os.rename(LIBRARY + book_title, dest_path)
    print(author + '/' + book_title)
