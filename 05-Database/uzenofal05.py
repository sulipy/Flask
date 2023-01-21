from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from data import courses
from forms import NewCourseForm

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fshghb162167t8jvbnodbndnb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)


# with app.app_context():
#     db.create_all()
#     for course in courses:
#         course_obj = Course(title=course['title'], teacher=course['teacher'], date=course['date'])
#         db.session.add(course_obj)
#     db.session.commit()
#     print(Course.query.all())


@app.route('/')
@app.route('/home')
def home():
    courses_db = db.session.execute(db.select(Course)).scalars()
    return render_template('courses.html', courses=courses_db, title='Üzenőfal')


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
            current_course = Course(title=form.title.data, teacher=form.teacher.data, date=form.date.data)
            db.session.add(current_course)
            db.session.commit()
            flash('A kurzus a megadott adatokkal mentésre került!', 'success')
            return redirect(url_for('home'))
    return render_template('create.html', title='Új kurzus létrehozása', form=form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
