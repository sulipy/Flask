from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from uzenofal.models import User


class NewCourseForm(FlaskForm):
    title = StringField('A kurzus címe', validators=[DataRequired(), Length(min=1, max=30)])
    teacher = StringField('Tanár', validators=[DataRequired(), Length(min=3, max=30)])
    date = DateField('Kezdés dátuma', validators=[DataRequired()])
    submit = SubmitField('Mentés')


class NewUserForm(FlaskForm):
    username = StringField('Név', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail cím', validators=[DataRequired(), Email(message='A megadott e-mail cím formailag nem megfelelő!')])
    password = PasswordField('Jelszó', validators=[DataRequired()])
    confirm_password = PasswordField('Jelszó még egyszer',
                                     validators=[DataRequired(), EqualTo('password', message='Nem egyezik meg a fent '
                                                                                             'megadott jelszóval')
                                                                       ])
    submit = SubmitField('Regisztráció')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ez a felhasználónév már foglalt. Adjon meg másikat!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ez az e-mail cím már foglalt. Adjon meg másikat!')
