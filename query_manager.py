from db_connection import connect_to_db


def save_new_user(user_name, password, connect):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s),(user_name, password);")
    cursor.close()
