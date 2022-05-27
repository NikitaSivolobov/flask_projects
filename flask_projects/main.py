from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
@app.route("/index")
def index():
    return render_template('index.html',
                           name='Никита',
                           title='Home page',
                           project_number=100)


if __name__ == '__main__':
    app.run(debug=True)