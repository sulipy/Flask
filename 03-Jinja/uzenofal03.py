from flask import Flask, redirect, url_for, render_template
from data import courses
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('courses.html', courses=courses, title='Üzenőfal')


@app.route('/message_board')
def message_board():
    return redirect(url_for('home'))


@app.route('/course/<int:number>')
def course(number):
    return f'Ez a {number}. kurzus adatlapja.'


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Elérhetőség')


@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime('%H:%S')
    return 'A pontos idő' + current_time


if __name__ == '__main__':
    app.run(debug=True)
