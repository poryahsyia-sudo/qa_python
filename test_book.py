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

#  Позитивный тест
    @pytest.mark.parametrize(
    'book_name, book_genre',
    [
       ('Тайны Коко', 'Фантастика'),
       ('Оно', 'Ужасы')
    ]
    )


    def test_set_book_genre_add_ganre_positive(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

#  Негативный тест

    @pytest.mark.parametrize(
    'book_name, book_genre',
    [
       ('Мара и Морок', 'Фэнтази'),
       ('Морозко', 'Сказка')
    ]
    )


    def test_set_book_genre_add_ganre_negative(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == ''

# Мои тесты на get_books_with_specific_genre
# Позитивнывй тест

    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Тайны Коко')
        collector.set_book_genre('Тайны Коко', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Тайны Коко']

# Негативный тест
    def test_get_books_with_specific_genre_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Морозко')
        collector.set_book_genre('Морозко', 'Сказка')
        assert collector.get_books_with_specific_genre('Мультфильмы') == []

# Мои тесты на get_books_genre
# Позитивнывй тест

    def  test_get_books_genre_return_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Тайны Коко')
        collector.set_book_genre('Тайны Коко', 'Фантастика')
        expected = {'Тайны Коко': 'Фантастика'}
        assert collector.get_books_genre() == expected


# Мои тесты на get_books_for_children
# Позитивнывй тест

    def  test_get_books_for_children_return_book_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        expected = ['Колобок']
        assert collector.get_books_for_children() == expected

# Мои тесты на add_book_in_favorites
# Позитивнывй тест
    def  test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_book_in_favorites('Дюна')
        expected = ['Дюна']
        assert collector.get_list_of_favorites_books() == expected

# Мои тесты на add_book_in_favorites
# Позитивнывй тест
    def  test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        expected = []
        assert collector.get_list_of_favorites_books() == expected

# Мои тесты на adget_list_of_favorites_books
# Позитивнывй тест на добавление в коллекцию 2-х книг

    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.add_book_in_favorites('Убийство в восточном экспрессе')
        collector.add_new_book('Верные враги')
        collector.add_book_in_favorites('Верные враги')
        assert collector.get_list_of_favorites_books() == ['Убийство в восточном экспрессе', 'Верные враги']

# Мои тесты на get_book_genre
# Негативный тест назапрос жанра несуществующей книги

    def  test_get_book_genre_for_unknown_book_returns_none(self):
        collector = BooksCollector()
        expected = None
        assert collector.get_book_genre('Письма незнакомке') == expected


