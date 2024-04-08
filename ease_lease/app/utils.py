from database import execute_query
def is_valid_login(username, password):
    SQL_QUERY = "SELECT * FROM users WHERE username = %s AND password = %s"
    result = execute_query(SQL_QUERY, (username, password))
    return len(result) == 1

def is_username_available(username):
    SQL_QUERY = "SELECT * FROM users WHERE username = %s"
    result = execute_query(SQL_QUERY, (username,))
    return len(result) == 0

def create_new_user(username, password):
    SQL_QUERY = "INSERT INTO users (username, password) VALUES (%s, %s)"
    result = execute_query(SQL_QUERY, (username, password))
    if result:
        return True
    return False

