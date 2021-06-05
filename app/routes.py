from app import app

@app.route('/')
@app.route('/index')
@app.route('/muffin')
def index():
  return "hello world!" 