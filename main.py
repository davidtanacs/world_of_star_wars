from flask import Flask, render_template, request
import requests
from db_connection import connect_to_db
from password_hash import hash

app = Flask(__name__)


page_num = 1


@app.route('/')
def show_table():
    global page_num
    if request.args.get('next'):
        page_num += 1
    elif request.args.get('previous'):
        page_num -= 1
    source = 'http://swapi.co/api/planets/?page={}'.format(page_num)
    response = requests.get(source).json()
    table = response['results']
    return render_template('table.html', table=table, page_num=page_num)


@app.route('/registration')
def registration():
    if request.args.get("username") and request.args.get("password"):
        username = request.args.get("username")
        password = request.args.get("password")
        password = hash(password)
    else:
        username = ""
        password = ""
    return render_template('registration.html', username=username, password=password)


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)