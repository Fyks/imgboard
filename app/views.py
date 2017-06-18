from flask import render_template
from app import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'kotya'}
    posts = [
        {
            'author': {'nickname': 'Dog'},
            'body': 'Woof! Woof!'
        },
        {
            'author': {'nickname': 'Bird'},
            'body': 'Tweet, motherfucker! Tweet!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/nya')
def nya():
    return render_template('nya.html',
                           title='Test')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
