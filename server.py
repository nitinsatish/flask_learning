from flask import Flask, render_template, request, redirect
from markupsafe import escape
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<string:username>')
def hello_user(username):
    return 'Hello, {}!'.format(escape(username))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return render_template('thanks.html', name=data['name'])
    else:
        return 'Something went wrong!'


# @app.route('/thanks', methods=['GET', 'POST'])
# def thanks(data):
#     return render_template('thanks.html', name=name)
