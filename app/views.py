from flask import render_template
from app import app


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
    return 'Nyaaa~'
