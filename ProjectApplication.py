import os.path
import pandas as pd
import glob
from flask import Flask, redirect, url_for, request, render_template
from jinja2 import Environment
from werkzeug.utils import secure_filename
from recipe_form import RecipeForm, SearchForm

# abs_path = os.path.abspath("static\\data_dir").replace("'", '"')
# os.chdir(abs_path)

os.chdir("C:\\Users\\Indigo\\Desktop\\Accelerated Software Development\\Term 2\\CP 1895\\Assignments\\Project\\static\\data_dir")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SUBMITTED_DATA'] = os.path.join("static", "data_dir", "")
app.config['SUBMITTED_IMG'] = os.path.join("static", "image_dir", "")
TEMPLATE_ENVIRONMENT = Environment(keep_trailing_newline=True)


@app.route('/')
def home_page():
    """
    Function to display home page
    :return:
    """
    return render_template('home_page.html')


@app.route('/add_recipe', methods=['POST', 'GET'])
def add_recipe():
    """
    Funtion to display add recipe page
    :return:
    """
    form = RecipeForm()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        recipe_ingredients = form.recipe_ingredients.data.lower()
        recipe_serving = form.recipe_serving.data
        recipe_instructions = form.recipe_instructions.data
        img_filename = recipe_name.lower().replace(" ", "_") + "." + \
                       secure_filename(form.recipe_img.data.filename).split('.')[-1]
        form.recipe_img.data.save(os.path.join(app.config['SUBMITTED_IMG'] + img_filename))
        df = pd.DataFrame([{'name': recipe_name, 'img': img_filename, 'ingredients': recipe_ingredients,
                            'serving': recipe_serving, 'instructions': recipe_instructions}], index=recipe_name)
        print(df)
        df.to_csv(os.path.join(app.config['SUBMITTED_DATA'] + recipe_name.lower().replace(" ", "_") + ".csv"))
        return redirect(url_for('home_page'))
    else:
        return render_template('add_recipe.html', form=form)


@app.route('/view_recipe/<name>')
def display_recipe(name):
    """
    Function to display a recipe
    :param name: Name of recipe
    :return:
    """
    df = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] +
                                  name.lower().replace(" ", "_") + ".csv"), index_col=False)
    print(df.iloc[0]['name'])
    return render_template('view_recipe.html', recipe=df.iloc[0])


@app.route('/search_recipe', methods=['POST', 'GET'])
def search_recipe():
    """
    Function to display a page for searching for a recipe
    :return:
    """
    form = SearchForm()
    extension = 'csv'

    if form.validate_on_submit():
        search = form.search.data.upper().lower()

        all_recipes = [i for i in glob.glob('*.{}'.format(extension))]
        combined_recipes = pd.concat([pd.read_csv(f, usecols=['name', 'ingredients'])
                                      for f in all_recipes])
        contains_ingredients = combined_recipes[combined_recipes['ingredients'].apply(lambda x: search in x)]
        contains_name = combined_recipes[combined_recipes['name'].apply(lambda x: search in x)]
        found_results = pd.concat([contains_name, contains_ingredients])

        print(search)
        print(contains_ingredients)
        print(contains_name)
        print()
        print(found_results)

        return render_template('search_results.html', recipe=found_results.iloc[0:100])
    else:
        return render_template('search_recipe.html', form=form)


@app.route('/results')
def results(recipes):
    """
    Function to display search results
    :return:
    """
    return render_template('search_results.html', recipe=recipes)


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
