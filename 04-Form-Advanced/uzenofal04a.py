from flask import Flask, redirect, url_for, render_template, request, flash
from data import courses
from forms import NewCourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fshghb162167t8jvbnodbndnb'


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


@app.route('/course/new', methods=['GET', 'POST'])
def create():
    form = NewCourseForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            courses.append({'title': form.title.data, 'teacher': form.teacher.data, 'date': form.date.data})
            flash('A kurzus a megadott adatokkal mentésre került!', 'success')
            return redirect(url_for('home'))
    return render_template('create.html', title='Új kurzus létrehozása', form=form)


if __name__ == '__main__':
    app.run(debug=True)
