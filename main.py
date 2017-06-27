from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def main():
    show_table()


@app.route('/')
def show_table():
    response = requests.get('http://swapi.co/api/planets/').json()
    table = response['results']
    return render_template('table.html', table=table)









if __name__ == '__main__':
    app.run(debug=True)