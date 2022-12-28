from flask import Flask, render_template, request, redirect, session, flash, url_for
from controller import auth
import calendar

from database import create_db_and_tables


app = Flask(__name__)

SECRET_KEY = 'moredevs'

create_db_and_tables()

from views.views import *

if __name__ == '__main__' :
    app.run(debug=True)