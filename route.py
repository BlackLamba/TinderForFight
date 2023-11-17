from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os
import mysql.connector
import register

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/templates/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(base_dir, 'templates'), filename)

@app.route('/')
def index():
    return render_template('site.html')

@app.route('/swipe.html')
def swipe():
    return render_template('swipe.html')

@app.route('/search.html')
def search():
    return render_template('bebra.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/onas.html')
def onas():
    return render_template('onas.html')



connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='~gZviBgh4AcOaK*3k$WP',
    database='users'  
)


cursor = connection.cursor()


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        register.register_user(username, password)  

        return redirect(url_for('profile'))  
    return render_template('register.html')  

if __name__ == '__main__':
    app.run(debug=True)
