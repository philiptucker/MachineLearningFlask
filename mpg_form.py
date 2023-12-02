from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class MPGForm(FlaskForm):
    cylinders = StringField('Cylinders: ', validators=[DataRequired()])
    displacement = StringField('Displacement: ', validators=[DataRequired()])
    horsepower = StringField('Horsepower: ', validators=[DataRequired()])
    weight = StringField('Weight: ', validators=[DataRequired()])
    acceleration = StringField('Acceleration: ', validators=[DataRequired()])
    model_year = StringField('Model Year: ', validators=[DataRequired()])
    origin = StringField('Country of Origin: ', validators=[DataRequired()])

