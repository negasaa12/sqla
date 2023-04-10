

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///outer_space'

app.app_context().push()

db = SQLAlchemy()
db.app = app
db.init_app(app)



app.config['SECRET_KEY'] = "HELLO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home():

    return render_template('home.html')