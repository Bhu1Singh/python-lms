from os import system, name

import datetime

def Clear():
    if name == "nt":
        _ = system('cls')

def WelcomeMsg():
    print("****************************************")
    print("Welcome to the Library Management System")
    print("****************************************")


def MainOptions():
    print("Choose from the following optios:\n 1 -> Issue a book \n "
            "2 -> Return a book \n 3 -> Search a book \n 4 -> Add new book \n 5 -> Manager User \n 6 -> Exit" )


def UserOptions():
    print("Choose from the following options: \n 1 -> Search User \n 2 -> Register new user \n"
            " 3 -> Delete User \n 4 -> Search User History \n 5 -> Return to Main Menu ")


def print_user_results(users : list):
        if len(users) > 0:
                print("User ID\t\tUserName\t\tStatus\t\tRegistration\t\tDeletedOn")
                for user in users:
                        print("{}\t\t{}\t\t{}\t\t{:%Y-%m-%d}\t\t{}".format(user.userID, user.userName, user.Active,
                                user.userRegistrationDate
                                , datetime.date.strftime(user.userDeleteDate, "%Y-%m-%d") if user.userDeleteDate is not None else None
                                ))


def print_book_results(books : list):
        if len(books) > 0:
                print("Book ID\t\t\tName\t\t\tBookWriter\t\t\tIssues To")
                for book in books:
                        print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(book.bookID, book.bookName, book.bookWriter, book.bookIssuedTo))

def print_user_book_results(books : list):
        if len(books) > 0:
                print("Book ID\t\t\tName\t\t\tStatus\t\t\tIssue Date\t\t\tReturn Date")
                for book in books:
                        print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(book.bookID, book.bookName, book.bookIssueStatus
                                , datetime.date.strftime(book.bookIssuedOn, "%Y-%m-%d") if book.bookIssuedOn is not None else None
                                , datetime.date.strftime(book.bookReturnDate, "%Y-%m-%d") if book.bookReturnDate is not None else None
                                ))