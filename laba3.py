class Writer:
    def __init__(self, name):
        self.name = name
        self.books = []

    def write_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f'{self.name}'

class Book:
    def __init__(self, title, plot, genre, kind):
        self.title = title
        self.plot = plot
        self.genre = genre
        self.kind = kind

    def __str__(self):
        return f'{self.title}'

writers_data = [
    {'name': 'Джордж Оруэлл', 'books': [('Доздравтвует фикус', 'трагикомедия', 'эпос', 'художественная литература'), ('Дни в Бирме', 'трагикомедия', 'драмма', 'художественная литература')]},
    {'name': 'Братья Стругацкие', 'books': [('Контрапункт', 'трагикомедия', 'эпос', 'художественная литература'), ('Стажеры', 'трагикомедия', 'драмма', 'художественная литература')]},
    {'name': 'Зигмунт Фрейд', 'books': [('Путь к основанию', 'трагикомедия', 'эпос', 'художественная литература'), ('Тотем и Табу', 'трагикомедия', 'драмма', 'художественная литература')]},
    {'name': 'Гегель', 'books': [('Философия духа', 'гуманитарные науки', 'психология', 'научно популярная литература')]}
]

# Создаем писателей и их книги
writers = {writer['name']: Writer(writer['name']) for writer in writers_data}
for writer_info in writers_data:
    writer = writers[writer_info['name']]
    for book_data in writer_info['books']:
        writer.write_book(Book(*book_data))

# Связи между понятиями о книгах, писателях и жанрах
relations = [
    {'from': '1', 'to': '15', 'type': 'is-a'},  # Пример связи

    # Связи между писателями и книгами
    {'from': 'Джордж Оруэлл', 'to': 'Доздравтвует фикус', 'type': 'has-written'},
    {'from': 'Джордж Оруэлл', 'to': 'Дни в Бирме', 'type': 'has-written'},
    {'from': 'Братья Стругацкие', 'to': 'Контрапункт', 'type': 'has-written'},
    {'from': 'Братья Стругацкие', 'to': 'Стажеры', 'type': 'has-written'},
    {'from': 'Зигмунт Фрейд', 'to': 'Путь к основанию', 'type': 'has-written'},
    {'from': 'Зигмунт Фрейд', 'to': 'Тотем и Табу', 'type': 'has-written'},
    {'from': 'Гегель', 'to': 'Философия духа', 'type': 'has-written'},

    # Связи между книгами и жанрами
    {'from': 'Доздравтвует фикус', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Доздравтвует фикус', 'to': 'эпос', 'type': 'is-a'},
    {'from': 'Доздравтвует фикус', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Дни в Бирме', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Дни в Бирме', 'to': 'драмма', 'type': 'is-a'},
    {'from': 'Дни в Бирме', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Контрапункт', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Контрапункт', 'to': 'эпос', 'type': 'is-a'},
    {'from': 'Контрапункт', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Стажеры', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Стажеры', 'to': 'драмма', 'type': 'is-a'},
    {'from': 'Стажеры', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Путь к основанию', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Путь к основанию', 'to': 'эпос', 'type': 'is-a'},
    {'from': 'Путь к основанию', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Тотем и Табу', 'to': 'трагикомедия', 'type': 'is-a'},
    {'from': 'Тотем и Табу', 'to': 'драмма', 'type': 'is-a'},
    {'from': 'Тотем и Табу', 'to': 'художественная литература', 'type': 'is-a'},
    {'from': 'Парень из приисподней', 'to': 'гуманитарные науки', 'type': 'is-a'},
    {'from': 'Парень из приисподней', 'to': 'психология', 'type': 'is-a'},
    {'from': 'Парень из приисподней', 'to': 'научно популярная литература', 'type': 'is-a'},
    {'from': 'Ответ Иову', 'to': 'гуманитарные науки', 'type': 'is-a'},
    {'from': 'Ответ Иову', 'to': 'психология', 'type': 'is-a'},
    {'from': 'Ответ Иову', 'to': 'научно популярная литература', 'type': 'is-a'},
    {'from': 'Философия духа', 'to': 'гуманитарные науки', 'type': 'is-a'},
    {'from': 'Философия духа', 'to': 'психология', 'type': 'is-a'},
    {'from': 'Философия духа', 'to': 'научно популярная литература', 'type': 'is-a'},
    {'from': 'Хакинг на LINUX', 'to': 'технические науки', 'type': 'is-a'},
    {'from': 'Хакинг на LINUX', 'to': 'наука и техника', 'type': 'is-a'},
    {'from': 'Хакинг на LINUX', 'to': 'научно популярная литература', 'type': 'is-a'},
    {'from': 'До последнего винтика', 'to': 'технические науки', 'type': 'is-a'},
    {'from': 'До последнего винтика', 'to': 'наука и техника', 'type': 'is-a'},
    {'from': 'До последнего винтика', 'to': 'научно популярная литература', 'type': 'is-a'},
    {'from': 'Многопоточные JS', 'to': 'технические науки', 'type': 'is-a'},
    {'from': 'Многопоточные JS', 'to': 'наука и техника', 'type': 'is-a'},
    {'from': 'Многопоточные JS', 'to': 'научно популярная литература', 'type': 'is-a'},

]

# Функции для ответа на вопросы
def get_genre_by_book_title(title):
    for writer in writers.values():
        for book in writer.books:
            if book.title.lower() == title.lower():
                return f"Жанр книги '{title}' - {book.genre}"
    return f"Не удалось найти информацию о книге '{title}'"

def get_books_by_writer(name):
    if name in writers:
        writer = writers[name]
        return f"Писатель {name} написал: {[book.title for book in writer.books]}"
    return f"Не удалось найти информацию о писателе {name}"

def get_books_by_genre(genre):
    books = []
    for writer in writers.values():
        for book in writer.books:
            if book.genre.lower() == genre.lower():
                books.append(book.title)
    return f"Книги жанра '{genre}': {books}"

# Примеры использования функций для ответа на вопросы
print("1. Введите название книги, чтобы узнать её жанр:")
book_title = input()
print(get_genre_by_book_title(book_title))

print("\n2. Введите имя писателя, чтобы узнать, какие книги он написал:")
writer_name = input()
print(get_books_by_writer(writer_name))

print("\n3. Введите жанр, чтобы узнать книги этого жанра:")
genre = input()
print(get_books_by_genre(genre))
