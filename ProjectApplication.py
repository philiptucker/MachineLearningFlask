import os.path
import pandas as pd
import datetime
from flask import Flask, redirect, url_for, render_template
from mpg_form import MPGForm
from diabetes_form import DiabetesForm
from joblib import load
from sklearn.linear_model import LinearRegression, LogisticRegression


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
        # TODO adjust for models params: cylinder, horsepower, weight, age, origin_japan, origin_usa
        cylinders = form.cylinders.data
        displacement = form.displacement.data
        horsepower = form.horsepower.data
        weight = form.weight.data
        acceleration = form.acceleration.data
        model_year = form.model_year.data
        origin_usa = 0
        origin_japan = 0
        if form.origin.data.casefold() == "usa":
            origin_usa = 1
        elif form.origin.data.casefold() == "japan":
            origin_japan = 1

        df = pd.DataFrame([{'cylinders': cylinders, 'horsepower': horsepower,
                            'weight': weight, 'age': (datetime.date.today().year - int(model_year)),
                            'origin_japan': origin_japan, 'origin_usa': origin_usa}])

        lm_model = load('mpg_model.joblib')
        mpg_predict = lm_model.predict(df)

        print((round(mpg_predict[0], 1)))
        # 16  6 	100.0 	3278 	50 	0 	1

        # return redirect(url_for('home_page'))
        return render_template('mpg_results.html', mpg=(round(mpg_predict[0], 1)), df=df)
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
        # TODO adjust for models params: Pregnancies, Glucose, SkinThickness, Insulin, BMI, Age
        pregnancies = form.pregnancies.data
        glucose = form.glucose.data
        bloodPressure = form.bloodPressure.data
        skinThickness = form.skinThickness.data
        insulin = form.insulin.data
        bmi = form.bmi.data
        age = form.age.data
        diabetesPedigreeFunction = form.diabetesPedigreeFunction.data

        df = pd.DataFrame([{'Pregnancies': pregnancies, 'Glucose': glucose, 'SkinThickness': skinThickness,
                            'Insulin': insulin, 'BMI': bmi, 'Age': age}])

        logr_model = load('diabetes_model.joblib')
        diabetes_predict = logr_model.predict(df)

        print(diabetes_predict[0])
        # 0  1 	109 	21 	135 	25.2 	23

        return render_template('diabetes_results.html', diabetes=diabetes_predict[0], df=df)
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
