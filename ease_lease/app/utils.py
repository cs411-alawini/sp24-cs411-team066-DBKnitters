from app.database import execute_query

def is_valid_login(username, password):
    SQL_QUERY = "SELECT * FROM User WHERE user_name = %s AND password = %s"
    result = execute_query(SQL_QUERY, (username, password))
    return len(result) == 1

def is_username_available(username):
    SQL_QUERY = "SELECT * FROM User WHERE user_name = %s"
    result = execute_query(SQL_QUERY, (username,))
    return len(result) == 0

def create_new_user(username, password, phone_number, first_name, last_name):
    SQL_QUERY = "INSERT INTO User (user_name, password, phone_number, first_name, last_name) VALUES (%s, %s, %s, %s, %s)"
    result = execute_query(SQL_QUERY, (username, password, phone_number, first_name, last_name))
    if result:
        return True
    return False
