import pymysql 

def get_db_connection():
    connection = pymysql.connect(
        host='34.171.144.159',
        user='root',
        password='cs411pt1066',
        database='ease_lease',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def execute_query(query, params=None):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()
        result = cursor.fetchall()
    connection.close()
    return result





