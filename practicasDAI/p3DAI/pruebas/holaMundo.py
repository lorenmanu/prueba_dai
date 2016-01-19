from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def hello_world(user=None):
    return render_template('hello.html',usuario=user)

if __name__ == '__main__':
    app.run(debug=True)
