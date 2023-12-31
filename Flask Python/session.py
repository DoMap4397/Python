from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Test'
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        session.permanent = True
        if user_name:
            session['user'] = user_name
            flash('Đã đăng nhập thành công!', 'info')
            return redirect(url_for('hello_user', name=user_name))
    if 'user' in session:
        name = session['user']
        flash('Đăng nhập không thành công!', 'info')
        return render_template('user.html', user=name)
    return render_template('login.html')


@app.route('/user')
def hello_user():
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
    app.run(debug=True)
