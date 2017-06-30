from db_connection import connect_to_db
from password_hash import check_password_hash


def save_new_user(username, password, connect):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s);", (username, password))
    cursor.close()


def user_login(username, password, connect):
    cursor = connect.cursor()
    cursor.execute("SELECT password FROM users WHERE username='%s';" % username)
    rows = cursor.fetchall()
    cursor.close()
    try:
        hashed_password = rows[0][0]
        username_check = True
    except IndexError:
        username_check = False
        hashed_password = ""
    if check_password_hash(hashed_password, password):
        password_check = True
    else:
        password_check = False
    if password_check and username_check:
        result = True
    else:
        result = False
    return result
