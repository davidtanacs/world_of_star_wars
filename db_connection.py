import psycopg2
import config


def connect_to_db():
    try:
        connect_str = ("dbname='{}' user='{}' host='localhost' password='{}'".format(
            config.dbname, config.user, config.password))
        connect = psycopg2.connect(connect_str)
        connect.autocommit = True
    except psycopg2.Error:
        print("Hey buddy, you made mistake(s) in config.py.")
    return connect