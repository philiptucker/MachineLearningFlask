import os.path

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd

from recipe_form import RecipeForm

app = Flask(__name__)


@app.route('/')
def home_page():
    """
    Function to display home page
    :return:
    """
    return render_template('home_page.html')


@app.route('/add_recipe')
def add_recipe():
    """
    Funtion to display add recipe page
    :return:
    """
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        recipe_ingredients = form.recipe_ingredients.data
        recipe_serving = form.recipe_serving.data
        recipe_instructions = form.recipe_instructions.data
        img_filename = recipe_name.lower().replace(" ", "_") + "." + \
                       secure_filename(form.recipe_img.filename).split('.')[-1]
        form.recipe_img.data.save(os.path.join(app.config['SUBMITTED_IMG'] + img_filename))
        df = pd.DataFrame({'Name: ': recipe_name, 'Ingredients: ': recipe_ingredients,
                           'Serving Size: ': recipe_serving, 'Instructions: ': recipe_instructions})
        df.to_csv(os.path.join(app.config['SUBMITTED_IMG'] + recipe_name.lower().replace(" ", "_") + ".csv"))
        print(df)
        return redirect(url_for('home_page'))
    else:
        return render_template('add_recipe.html', form=form)


@app.route('/view_recipe/<name>')
def display_recipe(name):
    df = pd.read_csv(os.path.join(app.config['SUBMITTED_IMG'] + name.lower().replace(" ", "_") + ".csv"))
    print(df.iloc[0]['name'])
    return render_template('view_recipe.html', recipe=df.iloc[0])


if __name__ == "__main__":
    app.run(debug=True)
