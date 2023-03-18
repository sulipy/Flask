from uzenofal import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)