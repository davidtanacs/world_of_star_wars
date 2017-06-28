from flask import Flask, render_template, request
import requests

app = Flask(__name__)


page_num = 1


def main():
    show_table()


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

if __name__ == '__main__':
    app.run(debug=True)