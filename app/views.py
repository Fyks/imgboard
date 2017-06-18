from flask import render_template, flash, redirect
from app import app
from app.form import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="' +
              form.openid.data +
              '", remember_me=' +
              str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
