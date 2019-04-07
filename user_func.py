from lib_users import users

from user_db_func import *

from book_db_func import search_book_history_user

from message_print import *

def handle_add_new_user():
    user_name = ''
    while True:
        user_name = input("Enter the user name: ")
        if len(user_name) > 0 and str.strip(user_name) != '':
            break
        print('User name is mandatory!')

    add_user(user_name)

    while True:
        nxt = input("Enter 1 to add another user and 9 to return to menu: ")

        if nxt == '1':
            handle_add_new_user()
            break
        elif nxt == '9':
            return

def handle_delete_user():
    user_id = ''
    while True:
        user_id = input("Enter the user id: ")
        if len(user_id) > 0 and str.strip(user_id) != '':
            break
        print('User ID is mandatory!')
        check = input("Enter 9 to return to previous menu or press any key to search again: ")
        if check == '9':
            return

    result = delete_user(user_id)
    print (result)
    
    while True:
        nxt = input("Enter 1 to delete another user and 9 to return to main menu: ")

        if nxt == '1':
            handle_delete_user()
            break
        elif nxt == '9':
            return

def handle_user_search():
    user_search = ''
    while True:
        user_search = input("Enter the user name: ")
        if len(user_search) > 0 and str.strip(user_search) != '':
            break
        print('Search string is mandatory!')
    
    result = search_user(user_search)
    print_user_results(result)

    user_id = input ('Enter User ID to view book issue history or press enter key to continue: ')

    result = search_book_history_user(user_id)
    print_user_book_results(result)

    print("\n")
    while True:
        nxt =     input("Enter 1 for new search and Press any other key to return to main menu...")

        if nxt == '1':
            handle_user_search()
            break
        else :
            return    