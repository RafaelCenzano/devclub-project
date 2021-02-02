from project import app
from flask import render_template, url_for

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/list')
def listThings():
  names = ['Elon Musk', 'Bill Gates', 'Mark Zuckerberg']
  return render_template('names.html', names=names)