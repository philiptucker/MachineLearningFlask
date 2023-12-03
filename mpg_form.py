from flask_wtf import FlaskForm
from wtforms.fields import DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired


class MPGForm(FlaskForm):
    cylinders = IntegerField('Cylinders: ', validators=[DataRequired()])
    displacement = DecimalField('Displacement: ', validators=[DataRequired()])
    horsepower = DecimalField('Horsepower: ', validators=[DataRequired()])
    weight = DecimalField('Weight: ', validators=[DataRequired()])
    acceleration = DecimalField('Acceleration: ', validators=[DataRequired()])
    model_year = IntegerField('Model Year: ', validators=[DataRequired()])
    origin = SelectField('Country of Origin: ',
                         choices=[('usa', 'usa'),
                                  ('japan', 'japan'),
                                  ('europe', 'europe')],
                         validators=[DataRequired()])

