import psycopg2
from config import dbname, user, password
import os
import urllib


def connect_to_db():
    try:
        connect_str = ("dbname='{}' user='{}' host='localhost' password='{}'".format(
            dbname, user, password))
        connect = psycopg2.connect(connect_str)
        connect.autocommit = True
    except psycopg2.Error:
        print("Hey buddy, you made mistake(s) in config.py.")
    return connect


urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
connection = psycopg2.connect(
    database=dbname,
    user=user,
    password=password,
    host='localhost',
    port=url.port
)