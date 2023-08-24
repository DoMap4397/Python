from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(seconds=10)

db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/home')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        session.permanent = True
        if user_name:
            session['user'] = user_name
            flash('Đã đăng nhập thành công!', 'info')
            return redirect(url_for('user', name=user_name))
    if 'user' in session:
        name = session['user']
        flash('Đăng nhập không thành công!', 'info')
        return redirect(url_for('user', name=user_name))
    return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        name = session['user']
        return render_template('user.html', user=name)
    else:
        flash('Bạn chưa đăng nhập!', 'info')
        return redirect(url_for('login'))


@app.route('/logout')
def log_out():
    flash('Đã đăng xuất thành công!', 'info')
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    if not path.exists('user.db'):
        db.create_all(app = app)
        print('Created database')
    app.run(debug=True)
