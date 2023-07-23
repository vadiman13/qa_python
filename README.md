# TestBooksCollector
### Описание

Этот проект содержит автоматизированные тесты для проверки функциональности класса BooksCollector с использованием фреймворка Pytest.

### Запуск автотестов

Чтобы запустить автотесты, выполните следующую команду:

pytest -v tests.py


### Структура проекта

- main.py - основной файл, содержащий класс BooksCollector и его методы.
- tests.py - файл, содержащий автотесты для класса BooksCollector.

### Описание автотестов

#### Тест добавления новой книги и установки рейтинга

def test_set_book_rating(self, book, rating):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.set_book_rating(book, rating)

    # Assert
    assert collector.get_book_rating(book) == rating


Этот тест проверяет корректность добавления новой книги в коллекцию и установки ей рейтинга.

#### Тест получения рейтинга книги

def test_get_books_rating(self, book, expected_rating):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.set_book_rating(book, expected_rating)
    books_rating = collector.get_books_rating()

    # Assert
    assert books_rating == {book: expected_rating}


Этот тест проверяет, что метод get_books_rating возвращает корректный словарь с рейтингами книг.

#### Тест добавления книги в избранное

def test_add_book_in_favorites(self, book):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.add_book_in_favorites(book)

    # Assert
    assert collector.get_list_of_favorites_books() == [book]


Этот тест проверяет, что метод add_book_in_favorites правильно добавляет книгу в список избранных книг.

#### Тест удаления книги из избранного

def test_delete_book_from_favorites(self, book):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.add_book_in_favorites(book)
    collector.delete_book_from_favorites(book)

    # Assert
    assert collector.get_list_of_favorites_books() == []


Этот тест проверяет, что метод delete_book_from_favorites правильно удаляет книгу из списка избранных книг.

#### Тест установки недопустимого рейтинга книги

def test_set_invalid_book_rating(self, invalid_rating):
    # Arrange
    collector = BooksCollector()
    book = "Гарри Поттер"

    # Act
    collector.add_new_book(book)
    collector.set_book_rating(book, invalid_rating)

    # Assert
    assert collector.get_book_rating(book) <= 10


Этот тест проверяет, что метод set_book_rating корректно обрабатывает попытку установки недопустимого рейтинга книги.

#### Тест добавления существующей книги

def test_add_existing_book(self):
    # Arrange
    collector = BooksCollector()
    book = "Гарри Поттер"

    # Act
    collector.add_new_book(book)
    collector.add_new_book(book)

    # Assert
    assert collector.get_books_rating() == {book: 1}


Этот тест проверяет, что метод add_new_book корректно обрабатывает попытку добавления уже существующей книги.
