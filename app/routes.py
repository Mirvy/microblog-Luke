from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/muffin')
def index():
  user = {'username':'Luke'}
  return render_template('index.html',title="Home",user=user)