from db_connection import connect_to_db


def save_new_user(username, password, connect):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s);",(username, password))
    cursor.close()
