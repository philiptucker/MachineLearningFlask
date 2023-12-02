from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired


class MPGForm(FlaskForm):
    cylinders = StringField('Cylinders: ', validators=[DataRequired()])
    displacement = StringField('Displacement: ', validators=[DataRequired()])
    horsepower = StringField('Horsepower: ', validators=[DataRequired()])
    weight = StringField('Weight: ', validators=[DataRequired()])
    acceleration = StringField('Acceleration: ', validators=[DataRequired()])
    model_year = StringField('Model Year: ', validators=[DataRequired()])
    origin = StringField('Country of Origin: ', validators=[DataRequired()])


class SearchForm(FlaskForm):
    search = StringField('', validators=[DataRequired()])


class RemoveForm(FlaskForm):
    remove = StringField('', validators=[DataRequired()])
