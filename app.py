from flask import Flask, render_template, url_for, flash, redirect
from forms import registration_form, login_form
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hi'
posts = [
    {
        'author': 'isaac reyes',
        'title': 'Post 1',
        'content': 'I am first post',
        'date_posted': 'April 19, 2024'
    },
    {
        'author': 'joe reyes',
        'title': 'Post 2',
        'content': 'I am second post',
        'date_posted': 'April 20, 2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
