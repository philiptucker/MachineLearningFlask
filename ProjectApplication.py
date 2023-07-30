import os.path

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home_page():
    """
    Function to display home page
    :return:
    """
    return render_template('home_page.html')


if __name__ == "__main__":
    app.run(debug=True)
