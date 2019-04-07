from books import books

from db_con import query_conn as query


def add_new_book(book : books) :
    try:
        query_str = "insert into books (BookName, BookWriter) values ('%s','%s')" % (book.bookName, book.bookWriter)
        result = query(query_str, False)
        print("Book has been added successfully: %s" % result)
    except Exception as err:
        print("An error has occured: %s" % err)

def search_book_by_name_or_id(search_string : str) -> list:
    try:
        query_str = ("select b.*,u.UserID from books b left join issuestatus i on b.bookid = i.bookid and i.issuestatus = 1"
                    + " left join users u on i.UserID = u.UserID"
                    + " where bookname like '%{}%' or b.bookid like '%{}%' "
                    + "or bookwriter like '%{}%'").format(search_string, search_string, search_string)
        result = query(query_str, True)
        return process_search_result(result)
    except Exception as err:
        print("An error has occured: %s", err)


def issue_book(book_id, user_id) -> str:
    try:
        query_str = "sp_issue_book '{}' , '{}'".format(book_id, user_id)
        result = query(query_str, True)
        return result
    except Exception as err:
        print("An error has occured: {}".format(err))


def return_book(book_id) -> str:
    try:
        query_str = "sp_return_book '{}'".format(book_id)
        result = query(query_str, True)
        return result
    except Exception as err:
        print("An error has occured: {}".format(err))


def search_book_history_user(user_id) -> list:
    try:
        query_str = ("select B.BookID, B.BookName, Case when I.IssueStatus = 1 then 'Issued' else 'Returned' end 'IssueStatus' "
                    + ", I.IssueDate, I.ReturnDate from Users U left join IssueStatus I on U.UserID = I.UserID"
                    + " left join Books B on I.BookID = B.BookID where U.UserID = '{}' "
                    + " order by I.IssueStatus desc, I.IssueDate desc").format(user_id)

        result = query(query_str,True)
        return process_search_history_result(result)
    except Exception as err:
        print("An error has occured: {}".format(err))


def process_search_result(book_result : list) -> list:
    book_list = []
    for row in book_result:
        book = books()
        book.bookID = row[0]
        book.bookName = row[1]
        book.bookWriter = row[2]
        book.bookRegistrationDate = row[3]
        book.bookIssuedTo = row[4]

        book_list.append(book) 

    return book_list

def process_search_history_result(book_result : list) -> list:
    book_list = []
    for row in book_result:
        book = books()
        book.bookID = row[0]
        book.bookName = row[1]
        book.bookIssueStatus = row[2]
        book.bookIssuedOn = row[3]
        book.bookReturnDate = row[4]

        book_list.append(book) 

    return book_list