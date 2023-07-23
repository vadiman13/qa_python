from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book, rating", [
        ("Гарри Поттер", 5),
        ("Властелин Колец", 4),
    ])
    def test_set_book_rating(self, book, rating):
        collector = BooksCollector()  # Создаем новый экземпляр BooksCollector для каждого теста
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)
        assert collector.get_book_rating(book) == rating

    @pytest.mark.parametrize("book, expected_rating", [
        ("Гарри Поттер", 5),
        ("Властелин Колец", 4),
    ])
    def test_get_books_rating(self, book, expected_rating):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_rating(book, expected_rating)
        books_rating = collector.get_books_rating()
        assert books_rating == {book: expected_rating}

    @pytest.mark.parametrize("book", [
        "Гарри Поттер",
        "Властелин Колец",
    ])
    def test_add_book_in_favorites(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    @pytest.mark.parametrize("book", [
        "Гарри Поттер",
        "Властелин Колец",
    ])
    def test_delete_book_from_favorites(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("invalid_rating", [
        15,
        20,
    ])
    def test_set_invalid_book_rating(self, invalid_rating):
        collector = BooksCollector()
        book = "Гарри Поттер"
        collector.add_new_book(book)
        collector.set_book_rating(book, invalid_rating)
        assert collector.get_book_rating(book) <= 10

    def test_add_existing_book(self):
        collector = BooksCollector()
        book = "Гарри Поттер"
        collector.add_new_book(book)
        collector.add_new_book(book)
        assert collector.get_books_rating() == {book: 1}
