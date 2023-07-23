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

def test_add_new_book(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")

    # Assert
    assert collector.get_books_rating() == {"Гарри Поттер":1}, "Книга или базовый рейтинг не добавлены"


Этот тест проверяет корректность добавления новой книги в коллекцию и установки ей начального рейтинга.

#### Тест повторного добавления книги

def test_add_existing_book(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Гарри Поттер")

    # Assert
    assert collector.get_books_rating() == {"Гарри Поттер": 1}, "Список избранных книг содержит дубликат"

Этот тест проверяет корректность повторного добавления книги на отсутствие дубля наименования и неизменности начального рейтинга.


#### Тест установления рейтинга книги

def test_set_book_rating(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.set_book_rating("Гарри Поттер", 1)

    # Assert
    assert collector.get_book_rating("Гарри Поттер") == 1, "Рейтинг отличается от выставленного"

Этот тест проверяет функциональность установления рейтинга книги на примере валидных значений.


#### Тест установления невалидного рейтинга книги

def test_set_book_rating(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.set_book_rating(name, rating)

    # Assert
    assert collector.get_book_rating(name) == 1, "Недопустимое значение рейтинга"

Этот тест проверяет функциональность установления рейтинга книги на примере невалидных значений.


#### Тест установления рейтинга не добавленной книги

def test_rate_unadded_book(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.set_book_rating("Неизвестная книга", 3)

    # Assert
    assert collector.get_book_rating(
        "Неизвестная книга") is None, "Рейтинг был установлен для книги, которая не была добавлена"

Этот тест проверяет работу метода при установке рейтинга книге, которая не была добавлена.



#### Тест получения рейтинга книги

def test_get_book_rating(self, book, expected_rating):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book(book)
    collector.set_book_rating(book,rating)

    # Assert
    assert collector.get_book_rating(book) == 5, "Неверный рейтинг книги"


Этот тест проверяет, что метод get_book_rating возвращает корректный рейтинг книги по имени.


#### Тест вывода словаря книг и рейтингов

def test_get_books_rating(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин колец")
    collector.set_book_rating("Гарри Поттер", 5)
    collector.set_book_rating("Властелин колец", 7)

    # Assert
    assert collector.get_books_rating() == {"Гарри Поттер": 5, "Властелин колец": 7}, "Неверный вывод словаря книга/рейтинг "

Этот тест проверяет, что метод get_books_rating корректно выводит словарь названий и рейтингов книг.


#### Тест вывода списка книг по рейтингу

def test_get_books_with_specific_rating(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Евгений Онегин")
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин колец")
    collector.set_book_rating("Евгений Онегин", 10)
    collector.set_book_rating("Гарри Поттер", 7)
    collector.set_book_rating("Властелин колец", 7)

    # Assert
    assert collector.get_books_with_specific_rating(7) == ["Гарри Поттер", "Властелин колец"], "Неверный списк книг с установленным рейтингом - результат поиска не соответствует рейтингу книг"

Этот тест проверяет возвращение списка книг методом get_books_with_specific_rating при поиске по значению рейтинга.


#### Тест вывода списка книг по рейтингу при поиске по отсутствующему в словаре значению

def test_get_books_with_no_specific_rating(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Евгений Онегин")
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин колец")
    collector.set_book_rating("Евгений Онегин", 10)
    collector.set_book_rating("Гарри Поттер", 7)
    collector.set_book_rating("Властелин колец", 7)

    # Assert
    assert collector.get_books_with_specific_rating(3) == [], "В списке присутствуют книги с рейтингом выше/ниже установленного"

Этот тест проверяет возвращение пустого списка книг методом get_books_with_specific_rating при поиске по отсутствующему в списке значению рейтинга.


#### Тест добавления книги в Избранное

def test_add_book_in_favorites(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")

    # Assert
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер"], "Выбранная книга не была добавлена в список Избранных"

Этот тест проверяет добавление книги в список Избранное add_book_in_favorites


#### Тест удаления книги и Избранного

def test_delete_book_from_favorites(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
 
    # Assert
    assert collector.get_list_of_favorites_books() == [], "Книга не была удалена из списка Избранных"

Этот тест проверяет удаление книги из списка Избранное методом delete_book_from_favorites


#### Тест вывода книги из списка Избранное

def test_get_list_of_favorites_books(self):
    # Arrange
    collector = BooksCollector()

    # Act
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Властелин колец")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.add_book_in_favorites("Властелин колец")

    # Assert
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер", "Властелин колец"], "Список избранных книг не выведен/выведен некорректно"

Этот тест проверяет get_list_of_favorites_books выводит корректный список Избранное