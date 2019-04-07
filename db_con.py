import pyodbc

conn_string = r"DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=test;UID=sa;PWD=Newuser123"

def query_conn(query : str, return_set : bool) -> list:
    conn = pyodbc.connect(conn_string, autocommit=True)
    cursor = conn.cursor()
    cursor.execute(query)
    if(return_set):
        result = cursor.fetchall()
    else:
        result = []
    conn.close()
    return result