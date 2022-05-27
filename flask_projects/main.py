from flask import Flask, render_template
from random import choice
random_name = choice(['Dasha', 'Elize', 'Rita', 'Nikita'])

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
@app.route("/index")
def index():
    return render_template('index.html',
                           name=random_name,
                           title='Home Page',
                           project_number=100)


if __name__ == '__main__':
    app.run(debug=True)