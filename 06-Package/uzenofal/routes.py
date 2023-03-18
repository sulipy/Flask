from flask import redirect, url_for, render_template, request, flash

from uzenofal import app, db
from uzenofal.models import Course
from uzenofal.data import courses
from uzenofal.forms import NewCourseForm


with app.app_context():
    db.create_all()
    for course in courses:
        course_obj = Course(title=course['title'], teacher=course['teacher'], date=course['date'])
        db.session.add(course_obj)
    db.session.commit()
    print(Course.query.all())


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



