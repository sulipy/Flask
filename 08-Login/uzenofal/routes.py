from flask import redirect, url_for, render_template, request, flash
from flask_login import login_user, current_user, login_required, logout_user

from uzenofal import app, db, bcrypt
from uzenofal.models import Course, User
from uzenofal.data import test_courses, test_users
from uzenofal.forms import NewCourseForm, NewUserForm, LoginForm


with app.app_context():
    db.create_all()
    for test_user in test_users:
        hashed_pswd = bcrypt.generate_password_hash('alma24').decode('utf-8')
        user_obj = User(username=test_user['username'], email=test_user['email'], password=hashed_pswd)
        db.session.add(user_obj)
    for test_course in test_courses:
        course_obj = Course(title=test_course['title'], date=test_course['date'], user_id=test_course['user_id'])
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = NewUserForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('A fiókod elkészült. Jelentkezz be!', 'success')
        print(User.query.all())
        return redirect(url_for('home'))
    return render_template('register.html', title='Felhasználói fiók létrehozása', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Bejelentkezés sikertelen. Ellenőrizd a megadott e-mail címet és jelszót!', 'danger')
    return render_template('login.html', title='Bejelentkezés', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Felhasználói fiók')