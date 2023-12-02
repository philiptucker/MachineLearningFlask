import os.path
import pandas as pd
from flask import Flask, redirect, url_for, render_template
from mpg_form import MPGForm
from diabetes_form import DiabetesForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaWCasdhaeAYGFSDG67893aehC4v5aB6aVavwev4545345v345v3SDFgdrg'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data_dir', '')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'image_dir', '')


@app.route('/')
def home_page():
    """
    Function to display home page
    :return:
    """
    return render_template('home_page.html')


@app.route('/test_mpg', methods=['POST', 'GET'])
def test_mpg():
    """
    Funtion to display test mpg page
    :return:
    """
    form = MPGForm()
    if form.validate_on_submit():

        cylinders = form.cylinders.data.casefold()
        displacement = form.displacement.data.casefold()
        horsepower = form.horsepower.data.casefold()
        weight = form.weight.data.casefold()
        acceleration = form.acceleration.data.casefold()
        origin = form.origin.data.casefold()
        model_year = form.model_year.data.casefold()

        df = pd.DataFrame([{'cylinders': cylinders, 'displacement': displacement, 'horsepower': horsepower,
                            'weight': weight, 'acceleration': acceleration, 'origin': origin,
                            'model_year': model_year}])
        print(df)

        return redirect(url_for('home_page'))
    else:
        return render_template('test_mpg.html', form=form)


@app.route('/test_diabetes', methods=['POST', 'GET'])
def test_diabetes():
    """
    Funtion to display test diabetes page
    :return:
    """
    form = DiabetesForm()
    if form.validate_on_submit():
        pregnancies = form.pregnancies.data.casefold()
        glucose = form.glucose.data.casefold()
        bloodPressure = form.bloodPressure.data.casefold()
        skinThickness = form.skinThickness.data.casefold()
        insulin = form.insulin.data.casefold()
        bmi = form.bmi.data.casefold()
        age = form.age.data.casefold()
        diabetesPedigreeFunction = form.diabetesPedigreeFunction.data.casefold()

        df = pd.DataFrame([{'pregnancies': pregnancies, 'glucose': glucose, 'bloodPressure': bloodPressure,
                            'skinThickness': skinThickness, 'insulin': insulin, 'bmi': bmi,
                            'age': age, 'diabetesPedigreeFunction': diabetesPedigreeFunction}])
        print(df)

        return redirect(url_for('home_page'))
    else:
        return render_template('test_diabetes.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    """
    Standard error handling
    :param e: Error details
    :return:
    """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
