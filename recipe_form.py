from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name: ', validators=[DataRequired()])
    recipe_img = FileField('Recipe Image: ', validators=[FileRequired()])
    recipe_ingredients = TextAreaField('Ingredients: ', validators=[DataRequired()])
    recipe_serving = StringField('Serving Size: ', validators=[DataRequired()])
    recipe_instructions = TextAreaField('Instructions: ', validators=[DataRequired()])


class SearchForm(FlaskForm):
    search = StringField('', validators=[DataRequired()])


class RemoveForm(FlaskForm):
    remove = StringField('', validators=[DataRequired()])
