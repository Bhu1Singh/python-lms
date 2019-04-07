from books import books

from book_db_func import *

from message_print import *

def handle_book_issue():
    book_id = ''
    while True:
        book_id = input("Enter the book id: ")
        if len(book_id) > 0 and str.strip(book_id) != '':
            break
        print('Book ID is mandatory!')

    
    user_id = ''
    while True:
        user_id = input('Enter user id: ')
        if len(user_id) > 0 and str.strip(user_id) != '':
            break
        print("User ID is mandatory!")

    result = issue_book(book_id, user_id)
    print(result)
    while True:
        nxt = input("Enter 1 to issue another book and 9 to return to main menu: ")

        if nxt == '1':
            handle_book_issue()
            break
        elif nxt == '9':
            return

def handle_book_return():
    book_id = ''
    while True:
        book_id = input("Enter the book id: ")
        if len(book_id) > 0 and str.strip(book_id) != '':
            break
        print('Book ID is mandatory!')

    result = return_book(book_id)
    print(result)
    while True:
        nxt = input("Enter 1 to return another book and 9 to return to main menu: ")

        if nxt == '1':
            handle_book_return()
            break
        elif nxt == '9':
            return

def handle_book_search():
    book_search = ''
    while True:
        book_search = input("Enter the book name or book ID or writer name (partial allowed) : ")
        if len(book_search) > 0 and str.strip(book_search) != '':
            break
        print('Search string is mandatory!')
    
    result = search_book_by_name_or_id(book_search)
    print_book_results(result)

    print("\n")
    while True:
        nxt =     input("Enter 1 for new search and Press any other key to return to main menu...")

        if nxt == '1':
            handle_book_search()
            break
        else :
            return    


def handle_book_search_history_user():
    user_id = ''
    while True:
        user_id = input("Enter the User ID (Exact): ")
        if len(user_id) > 0 and str.strip(user_id) != '':
            break
        print('User ID is mandatory!')
    
    result = search_book_history_user(user_id)
    print_user_book_results(result)

    print("\n")
    while True:
        nxt =     input("Enter 1 for new search and Press any other key to return to main menu...")

        if nxt == '1':
            handle_book_search_history_user()
            break
        else :
            return    


def handle_add_new_book():
    book_name = ''
    while True:
        book_name = input("Enter the book name: ")
        if len(book_name) > 0 and str.strip(book_name) != '':
            break
        print('Book name is mandatory!')

    
    book_writer = ''
    while True:
        book_writer = input('Enter book writer name: ')
        if len(book_writer) > 0 and str.strip(book_writer) != '':
            break
        print("Book writer is mandatory!")
    
    book = books()
    book.bookName = book_name
    book.bookWriter = book_writer

    add_new_book(book)

    print("\n")
    while True:
        nxt =     input("Enter 1 for adding another book or press any other key to return to main menu...")

        if nxt == '1':
            handle_add_new_book()
            break
        else :
            return    
