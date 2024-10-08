from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

# pip install flask and pip intstall flask_mysqldb for them to run

app = Flask(__name__)

app.secret_key = "created secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9667'
app.config['MYSQL_DB'] = 'PMREGISTER'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT* FROM accounts WHERE username = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email,))
            mysql.connection.commit()
            msg = "You have successfully registered !"
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route('/rtu')
def rtu():
    return render_template('rtu.html')


@app.route('/aktu')
def aktu():
    return render_template('aktu.html')

@app.route('/amity')
def amity():
    return render_template('amity.html')

@app.route('/jecrc')
def jecrc():
    return render_template('jecrc.html')

@app.route('/poornima')
def poornima():
    return render_template('poornima.html')

@app.route('/lnm')
def lnm():
    return render_template('lnm.html')

@app.route('/manipal')
def manipal():
    return render_template('manipal.html')

@app.route('/bits')
def bits():
    return render_template('bits.html')

@app.route('/birla')
def birla():
    return render_template('birla.html')

@app.route('/banasthali')
def banasthali():
    return render_template('banasthali.html')

@app.route('/sgv')
def sgv():
    return render_template('sgv.html')



if __name__ == '__main__':
    app.run(debug=True)
