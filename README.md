# qa_python  
## Тесты для приложения **BooksCollector**  
## 10 мая 2023 
### Пример теста 
#### Методы add_new_book, get_books_rating
	Проверяем возможность длбавления двух книг.

### тест 1   
#### Методы add_new_book, get_books_rating 
     Проверяем что нельзя добавить две новых книги с одинаковым названием 
### тест 2  
#### Методы set_new_book, add_new_book, get_books_rating    
	увеличиваем рейтинг  книги (от 1 до 10) которая уже есть в словаре books_rating  
### тест 3   
#### Методы add_new_book, set_new_book, get_books_rating  		
	Проверяем что нельзя добавить  книгу, если она уже существует в словаре books_rating, с рейтингом больше 1.  
### тесты 4-8  
#### Методы set_new_book, add_new_book, get_books_rating  
	изменяем рейтинг книги из books_rating,  вне дозволенного интервала [1-10], проверяем значения 0,-5, 15, 7.8, А.
### тест 9  
#### Метод get_books_rating  
	получаем рейтинг книги из books_rating по имени.
### тест 10  
#### Метод get_books_with_specific_rating  
	получаем  список книг с заданным рейтингом (3).  
### тест 11  
#### Метод get_books_with_specific_rating  
	получаем  список книг с заданным рейтингом (4) который отсутствует в books_rating.
### тест 12  
#### Метод get_books_rating  
	проверяем вывод не пустого books_rating.
### тест 13    
#### Метод get_books_rating  
	проверяем вывод пустого books_rating.
### тест 14    
#### Метод add_book_in_favorites, get_list_of_favorites_books  
	добавляем первую книгу в избранное.
### тест 15  
#### Метод add_book_in_favorites, get_list_of_favorites_books  
	добавляем первую книгу в избранное.
### тест 16  
#### Метод add_book_in_favorites, get_list_of_favorites_books  
	добавляем  книгу в избранное, кторой нет в books_rating.
### тест 17   
#### Метод delete_book_from_favorites, get_list_of_favorites_books  
	удаляем  книгу из избранное.
### тест 18   
#### Метод delete_book_from_favorites, get_list_of_favorites_books  
	удаляем  книгу из пустого списка избранное.
### тест 19  
#### Метод get_list_of_favorites_books  
	проверяем вывод списка избранное.