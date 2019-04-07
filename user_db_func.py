from lib_users import users

from db_con import query_conn as query


def add_user(user : str) :
    try:
        query_str = "insert into users (UserName) values ('%s')" % user
        result = query(query_str, False)
        print("User has been added successfully: %s" % result)
    except Exception as err:
        print("An error has occured: %s" % err)


def delete_user(user_id) -> str:
    try:
        query_str = "sp_delete_user '{}'".format(user_id)
        result = query(query_str, True)
        return result
    except Exception as err:
        print("An error has occured: %s" % err)


def search_user(search_string : str) -> list:
    try:
        query_str = "select * from Users where username like '%" + search_string + "%'"
        result = query(query_str, True)
        return process_search_result(result)
    except Exception as err:
        print("An error has occured: %s", err)


def process_search_result(user_result : list) -> list:
    user_list = []
    for row in user_result:
        user = users()
        user.userID = row[0]
        user.userName = row[1]
        user.Active = row[2]
        user.userRegistrationDate = row[3]
        user.userLastModification = row[4]
        user.userDeleteDate = row[5]

        user_list.append(user) 

    return user_list