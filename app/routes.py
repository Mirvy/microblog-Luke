from app import app

@app.route('/')
@app.route('/index')
@app.route('/muffin')
def index():
  user = {'username':'Luke'}
  return '''
<html>
  <head>
    <title>Home Page - Microblog</title>
  </head>
  <body>
    <h1>Hello, ''' + user['username'] + '''!</h1>
  </body>
</html>'''