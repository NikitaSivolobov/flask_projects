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

@app.route("/<float:num1>/<operation>/<float:num2>/")
def calculator_jinja(num1, operation, num2):
    return render_template('index.html',
                           num1=num1,
                           operation=operation,
                           num2=num2)

@app.route('/module3_lesson2_step5/')
def module3_lesson2_step5():
    return render_template(
        'module3_lesson2_step5.html',
    )

if __name__ == '__main__':
    app.run(debug=True)