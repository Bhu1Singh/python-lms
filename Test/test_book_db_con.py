import sys
sys.path.insert(0, 'd:\\Workspace\\Source\\git\\Python\\VSCode_Python')

from Python.LMS.books import books

from Python.LMS.book_db_func import add_new_book, search_book_by_name_or_id

from Python.LMS.message_print import print_book_results

def test_add_new_book(book_name : str, book_writer : str):
    book = books()
    book.bookName = book_name
    book.bookWriter = book_writer
    add_new_book(book)


def test_search_book_by_name_or_id(search_string : str):
    result = search_book_by_name_or_id(search_string)
    print_book_results(result)
    
test_search_book_by_name_or_id('1')