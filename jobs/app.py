from flask import Flask
from flask import render_template, helpers
from flask.globals import g
import sqlite3

PATH='db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if (connection == None):
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

