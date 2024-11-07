# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "Hello, Docker!"
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Wow'  # Set a secret key for session management

# Simple user data for demonstration
USERNAME = 'bits_admin'
PASSWORD = 'welcome'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return f'Welcome, {username}!'
        else:
            flash('Invalid credentials, please try again.')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

