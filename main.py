import message_print as msg

from book_func import *
from user_func import *

def main():
    msg.Clear()
    msg.WelcomeMsg()
    msg.MainOptions()

    option = int(input("Enter the number for the option to proceed: "))

    if option == 1:
        msg.Clear()
        handle_book_issue()
        main()

    elif option == 2:
        msg.Clear()
        handle_book_return()
        main()

    elif option == 3:
        msg.Clear()
        handle_book_search()
        main()

    elif option == 4:
        msg.Clear()
        handle_add_new_book()
        main()

    elif option == 5:
        handle_user_options()

    elif option == 6:
        return
        
    else :
        main()


def handle_user_options():
    msg.Clear()
    msg.UserOptions()
    option = int(input("Enter the number for the option to proceed: "))

    if option == 1:
        msg.Clear()
        handle_user_search()
        nxt = input ("Enter 1 to go back to user menu press anything to return to main menu: ")

        if nxt == '1':
            handle_user_options()
        else :
            main()
    
    elif option == 2:
        msg.Clear()
        handle_add_new_user()
        handle_user_options()

    elif option == 3:
        msg.Clear()
        handle_delete_user()
        handle_user_options()

    elif option == 4:
        msg.Clear()
        handle_book_search_history_user()
        handle_user_options()

    elif option == 5:
        main()

    else :
        handle_user_options()

if __name__ == "__main__": main()
        
