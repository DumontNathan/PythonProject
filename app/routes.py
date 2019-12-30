from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.model import User
from flask_login import login_user

posts = [
    {
        'author' : 'Nathan Dumont',
        'title' : 'Post number 1',
        'content' : 'First content',
        'date_posted' : 'December 20th 2019'
    },
    {
        'author' : 'Billy Jack',
        'title' : 'Post number 2',
        'content' : 'Second content',
        'date_posted' : 'December 20th 2019'
    }
]


@app.route('/')
@app.route('/home')
def index () :
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():    # = controller
    form = RegistrationForm()    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  #Hashing password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  #User creation
        db.session.add(user)                                                                #Preparing for commit
        db.session.commit()                                                                 #Commiting to database
        flash('Account created. You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful, check email/password', 'danger')    
    return render_template('login.html', title='Login', form=form)  