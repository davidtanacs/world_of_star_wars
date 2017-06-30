from flask import Flask, render_template, request, session, escape, redirect, url_for
import requests
from db_connection import connect_to_db
from password_hash import hash, check_password_hash
import query_manager
import secret_key_src

app = Flask(__name__)


page_num = 1


@app.route('/')
def show_table():
    global page_num
    if request.args.get('next'):
        if page_num < 7:
            page_num += 1
    elif request.args.get('previous'):
        if page_num > 1:
            page_num -= 1
    source = 'http://swapi.co/api/planets/?page={}'.format(page_num)
    response = requests.get(source).json()
    table = response['results']
    try:
        username = session['username']
    except KeyError:
        username = ""
    return render_template('table.html', table=table, page_num=page_num, username=username)


@app.route('/registration', methods=["GET", "POST"])
def registration():
    if request.form.get("username") and request.form.get("password"):
        username = request.form.get("username")
        password = request.form.get("password")
        password = hash(password)
        query_manager.save_new_user(username, password, connect_to_db())
        return redirect(url_for('show_table'))
    else:
        username = ""
        password = ""
    return render_template('registration.html', username=username, password=password)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.form.get("username") and request.form.get("password"):
        username = request.form.get("username")
        password = request.form.get("password")
        if query_manager.user_login(username, password, connect_to_db()):
            login = True
            session['username'] = username
            return redirect(url_for('show_table'))
        else:
            login = False
    login = False
    return render_template('login.html', login=login)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('show_table'))

if __name__ == '__main__':
    app.secret_key = secret_key_src.secret_key
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
