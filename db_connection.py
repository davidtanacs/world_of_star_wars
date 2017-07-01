import psycopg2
import os
import urllib


def connect_to_db():
    try:
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
        connection = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
                )
        connection.autocommit = True
    except psycopg2.Error:
        print("Hey buddy, you made mistake(s) in config.py.")
    return connection
