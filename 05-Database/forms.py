from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length


class NewCourseForm(FlaskForm):
    title = StringField('A kurzus címe', validators=[DataRequired(), Length(min=1, max=30)])
    teacher = StringField('Tanár', validators=[DataRequired(), Length(min=3, max=30)])
    date = DateField('Kezdés dátuma', validators=[DataRequired()])
    submit = SubmitField('Mentés')
