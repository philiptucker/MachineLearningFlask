from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class DiabetesForm(FlaskForm):
    pregnancies = StringField('Pregnancies: ', validators=[DataRequired()])
    glucose = StringField('Glucose: ', validators=[DataRequired()])
    bloodPressure = StringField('BloodPressure: ', validators=[DataRequired()])
    skinThickness = StringField('SkinThickness: ', validators=[DataRequired()])
    insulin = StringField('Insulin: ', validators=[DataRequired()])
    bmi = StringField('BMI: ', validators=[DataRequired()])
    age = StringField('Age: ', validators=[DataRequired()])
    diabetesPedigreeFunction = StringField('Diabetes Pedigree Function: ', validators=[DataRequired()])
