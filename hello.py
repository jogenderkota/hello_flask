from flask import Flask, flash, redirect, render_template, url_for, request

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
   return render_template('hello.html', name = name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'user %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash(u'Invalid password provided', 'error')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)
