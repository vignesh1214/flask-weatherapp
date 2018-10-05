from flask import Flask , render_template
import requests
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('weather.html')
