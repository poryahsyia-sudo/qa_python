import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Мои тесты  add_new_book на количество символов

    @pytest.mark.parametrize(
        'book_name',
        [
            ('Я '),                                       # длина 1 символ, добавляется
            ('Алиса в стране чудес чаепитие с кроликом'), # длина 40 символов, добавится
        ]
    )

    def test_add_new_book_with_allowed_title_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name',
        [
            ('Секреты затерянного города и древние тайны'), # длина 41 символов — не добавится
            (""),                                           # пустая строка — не добавится
        ]
    )

    def test_add_new_book_with_disallowed_title_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

# Мои тесты  set_book_genre

@pytest.mark.parametrize(
    'book_name, book_genre',
    [
       ('Тайны Коко', 'Фантастика'),
       ('Оно', 'Ужасы')
    ]
)

def test_set_book_genre_add_ganre(self, book_name, book_genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, book_genre)
    assert collector.get_book_genre(book_name) == book_genre