from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        assert collector.get_books_rating() == {"Гарри Поттер":1}, "Книга и/или базовый рейтинг не добавлены"

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Гарри Поттер")
        assert collector.get_books_rating() == {"Гарри Поттер": 1}, "Список избранных книг содержит дубликат"


    def test_set_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_rating("Гарри Поттер", 3)
        assert collector.get_book_rating("Гарри Поттер") == 3, "Рейтинг отличается от выставленного"


    @pytest.mark.parametrize("name, rating", [
        ("Гарри Поттер", -1),
        ("Гарри Поттер", 0),
        ("Гарри Поттер", 11),
    ])
    def test_set_invalid_book_rating(self, name, rating):
        collector = BooksCollector()
        book = "Гарри Поттер"
        collector.add_new_book(book)
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) == 1, "Недопустимое значение рейтинга"

    def test_rate_unadded_book(self):
        collector = BooksCollector()
        collector.set_book_rating("Неизвестная книга", 3)
        assert collector.get_book_rating(
            "Неизвестная книга") is None, "Рейтинг был установлен для книги, которая не была добавлена"

    def test_get_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_rating("Гарри Поттер",5)
        assert collector.get_book_rating("Гарри Поттер") == 5, "Неверный рейтинг книги"

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин колец")
        collector.set_book_rating("Гарри Поттер", 5)
        collector.set_book_rating("Властелин колец", 7)
        assert collector.get_books_rating() == {"Гарри Поттер": 5, "Властелин колец": 7}, "Неверный вывод словаря книга/рейтинг "

    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Евгений Онегин")
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин колец")
        collector.set_book_rating("Евгений Онегин", 10)
        collector.set_book_rating("Гарри Поттер", 7)
        collector.set_book_rating("Властелин колец", 7)
        assert collector.get_books_with_specific_rating(7) == ["Гарри Поттер", "Властелин колец"], "Неверный списк книг с установленным рейтингом - результат поиска не соответствует рейтингу книг"

    def test_get_books_with_no_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Евгений Онегин")
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин колец")
        collector.set_book_rating("Евгений Онегин", 10)
        collector.set_book_rating("Гарри Поттер", 7)
        collector.set_book_rating("Властелин колец", 7)
        assert collector.get_books_with_specific_rating(3) == [], "Выведен список с некорректными данными"

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"], "Выбранная книга не была добавлена в список Избранных"

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == [], "Книга не была удалена из списка Избранных"

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Властелин колец")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер", "Властелин колец"], "Список избранных книг не выведен/выведен некорректно"