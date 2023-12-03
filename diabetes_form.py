from flask_wtf import FlaskForm
from wtforms.fields import StringField, DecimalField, IntegerField
from wtforms.validators import DataRequired


class DiabetesForm(FlaskForm):
    pregnancies = IntegerField('Pregnancies: ', validators=[DataRequired()])
    glucose = DecimalField('Glucose: ', validators=[DataRequired()])
    bloodPressure = DecimalField('BloodPressure: ', validators=[DataRequired()])
    skinThickness = DecimalField('SkinThickness: ', validators=[DataRequired()])
    insulin = DecimalField('Insulin: ', validators=[DataRequired()])
    bmi = DecimalField('BMI: ', validators=[DataRequired()])
    age = IntegerField('Age: ', validators=[DataRequired()])
    diabetesPedigreeFunction = DecimalField('Diabetes Pedigree Function: ', validators=[DataRequired()])
