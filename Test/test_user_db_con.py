import sys
sys.path.insert(0, 'd:\\Workspace\\Source\\git\\Python\\VSCode_Python')

from Python.LMS.lib_users import users

from Python.LMS.user_db_func import add_user, delete_user, search_user

from Python.LMS.message_print import print_user_results

def test_user_addition(user_name : str):
    user = users()
    user.userName = user_name
    add_user(user)


def test_user_delete(user_id : int):
    delete_user(user_id)


def search_user_test(search_string : str):
    result = search_user(search_string)
    print_user_results(result)
    

search_user_test('n')

# test_user_addition("Rajshree")

#test_user_delete('7')
