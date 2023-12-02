import os.path
import pandas as pd
from flask import Flask, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from mpg_form import MPGForm, SearchForm, RemoveForm

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
    Funtion to display add recipe page
    :return:
    """
    form = MPGForm()
    if form.validate_on_submit():
        '''recipe_name = form.recipe_name.data.casefold()
        recipe_ingredients = form.recipe_ingredients.data.casefold()
        recipe_serving = form.recipe_serving.data
        recipe_instructions = form.recipe_instructions.data'''

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
    if form.validate_on_submit():
        search = form.search.data.casefold()

        all_recipes = os.listdir(app.config['SUBMITTED_DATA'])
        combined_recipes = pd.concat([pd.read_csv(app.config['SUBMITTED_DATA'] + f, usecols=['name', 'ingredients'])
                                      for f in all_recipes])

        contains_ingredients = combined_recipes[combined_recipes['ingredients'].apply(lambda x: search in x)]
        contains_name = combined_recipes[combined_recipes['name'].apply(lambda x: search in x)]
        found_results = pd.concat([contains_name, contains_ingredients])
        found_results = found_results.drop_duplicates()

        listedResults = found_results['name'].values.tolist()

        print(search)
        print(contains_ingredients)
        print(contains_name)
        print()
        print(found_results.iloc[:]['name'])
        print(listedResults)

        return render_template('search_results.html', recipe=listedResults, len=len(listedResults), search=search)
    else:
        return render_template('search_recipe.html', form=form)


@app.route('/remove_recipe', methods=['POST', 'GET'])
def remove_recipe():
    """
    Function to list all recipes and select one to remove
    :return:
    """
    all_recipes = os.listdir(app.config['SUBMITTED_DATA'])
    combined_recipes = pd.concat([pd.read_csv(app.config['SUBMITTED_DATA'] + f, usecols=['name', 'ingredients'])
                                  for f in all_recipes])

    listedResults = combined_recipes['name'].values.tolist()
    form = RemoveForm()
    if form.validate_on_submit():
        remove = form.remove.data.casefold()
        remove_csv = remove + ".csv"
        if os.path.isfile('static\\data_dir\\' + remove_csv):

            df = pd.read_csv(os.path.join(app.config['SUBMITTED_DATA'] + remove.lower().replace(" ", "_") + ".csv"),
                             index_col=False)

            remove_img = df.loc[0]['img']

            print(remove_csv + " + " + remove_img)

            print(os.listdir('static\\data_dir\\'))

            if os.path.isfile('static\\data_dir\\' + remove_csv):
                os.remove('static\\data_dir\\' + remove_csv)
                os.remove('static\\image_dir\\' + remove_img)
                print(f"{remove} has been removed from the list of recipes.")
            return render_template('removed.html', remove=remove, confirm="yes")
        else:
            print(f"The recipe: '{remove}' was not found.")
            return render_template('removed.html', remove=remove, confirm="no")
    else:
        return render_template('recipe_list.html', form=form, recipe=listedResults, len=len(listedResults))


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
