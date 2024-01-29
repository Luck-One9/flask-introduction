from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    return "<h2>Hello World!</h1>"

@app.route('/profile/<name>')
def teste(name=None):
    return render_template('index.html', name=name)