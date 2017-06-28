from werkzeug.security import generate_password_hash, check_password_hash


def hash(password):
    hashed_password = generate_password_hash(
        password)
    return hashed_password
