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
        assert len(collector.get_books_rating()) == 2

    # тест1
    # Проверяем что нельзя добавить две новых книги с одинаковым названием
    def test_add_new_book_the_same_books(self):
        collector = BooksCollector()
        # добавляем  книгу два раза
        collector.add_new_book('ЖЗЛ')
        collector.add_new_book('ЖЗЛ')
        # проверяем, что добавилось именно одна
        assert len(collector.get_books_rating()) == 1

    # тест2
    # увеличиваем рейтинг книги (от 1 до 10)
    def test_set_book_rating_add_books_rating1_and_upgrade_rating10(self):
        collector = BooksCollector()
        # добавляем  книгу  с рейтингом 1 и увеличиваем до 5
        collector.add_new_book('ЖЗЛ')
        collector.set_book_rating('ЖЗЛ', 5)

        # проверяем
        assert collector.get_book_rating('ЖЗЛ') == 5

    # тест3
    # Проверяем что нельзя добавить  книгу, если она уже существует с рейтингом больше 1
    def test_add_new_book_add_books_rating5(self):
        collector = BooksCollector()
        # добавляем  книгу  с рейтингом 5
        collector.add_new_book('ЖЗЛ')
        collector.set_book_rating('ЖЗЛ', 5)
        # добавляем эту же книгу  как новую
        collector.add_new_book('ЖЗЛ')
        # проверяем, что ничего не добавилось
        assert collector.get_book_rating('ЖЗЛ') == 5 and len(collector.get_books_rating()) == 1

    # тест4-8
    # изменяем рейтинг книги  вне дозволенного интервала [1-10]
    import pytest
    @pytest.mark.parametrize('ratin', [0, -5, 15, 7.8, 'A'])
    def test_set_book_rating_out_of_range(self, ratin):
        collector = BooksCollector()
        # добавляем  книгу  с рейтингом 1 и проверяем изменения рейтинга на 0, -5, 15, 7.8
        collector.add_new_book('ЖЗЛ')
        collector.set_book_rating('ЖЗЛ', ratin)

        # проверяем
        assert collector.get_book_rating('ЖЗЛ') == 1

    # тест9
    # получаем рейтинг по имени
    def test_get_book_rating_name_rating(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 2, 'хрю': 5}

        # проверяем
        assert collector.get_book_rating('гав') == 2

    # тест10
    # список книг с рейтингом 3
    def test_get_books_with_specific_rating_set_rating3(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}

        # проверяем
        assert collector.get_books_with_specific_rating(3) == ['гав', 'куку']

    # тест11
    # список книг с рейтингом 4 который отсутствует
    def test_get_books_with_specific_rating_no_rating4(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}

        # проверяем
        assert collector.get_books_with_specific_rating(4) == []

    # тест12
    # вывод словарь не пустой
    def test_get_books_rating_not_empty(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}

        # проверяем
        assert collector.get_books_rating() == collector.books_rating

    # тест13
    # вывод словарь  пустой
    def test_get_books_rating_empty(self):
        collector = BooksCollector()

        # проверяем
        assert collector.get_books_rating() == collector.books_rating

    # тест14
    # Добавляем   первую книгу в избранное
    def test_add_book_in_favorites_add_first_book(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}
        collector.add_book_in_favorites('хрю')
        # проверяем
        assert collector.get_list_of_favorites_books() == ['хрю']

    # тест15
    # Добавляем   не первую книгу в избранное

    def test_add_book_in_favorites_add_not_the_first_book(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}
        collector.favorites = ['мяу', 'гав']
        collector.add_book_in_favorites('хрю')
        # проверяем
        assert collector.get_list_of_favorites_books() == ['мяу', 'гав', 'хрю']

    # тест16
    # Добавляем    книгу в избранное которой нет в рейтинге
    def test_add_book_in_favorites_add_book_not_in_rating(self):
        collector = BooksCollector()
        collector.books_rating = {'мяу': 1, 'гав': 3, 'хрю': 5, 'куку': 3}
        collector.favorites = ['мяу', 'гав']
        collector.add_book_in_favorites('иа')
        # проверяем
        assert collector.get_list_of_favorites_books() == collector.favorites

    # тест17
    # Удаляем существующую книгу из избранного
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.favorites = ['мяу', 'гав']
        collector.delete_book_from_favorites('гав')
        # проверяем
        assert collector.get_list_of_favorites_books() == ['мяу']

    # тест18
    # Удаляем  книгу из пустого списка избранного
    def test_delete_book_from_favorites_delete_book_empty_list(self):
        collector = BooksCollector()
        collector.favorites = []
        collector.delete_book_from_favorites('гав')
        # проверяем
        assert collector.get_list_of_favorites_books() == []

    # тест19
    # Получаем список избранного
    def test_get_list_of_favorites_books_books_list(self):
        collector = BooksCollector()
        collector.favorites = ['мяу', 'гав']
        # проверяем
        assert collector.get_list_of_favorites_books() == collector.favorites
