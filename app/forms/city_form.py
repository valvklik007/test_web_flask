from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CityForm(FlaskForm):
    city = StringField('Город', validators=[DataRequired(message="Введите название города"), Length(min=2, max=100)])
    submit = SubmitField('Показать погоду')