from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hell_word():
    return '<h1> Python </h1>'


@app.route('/user/<name>')
def hell_user(name):
    return f'<h1> Hello {name}! </h1>'


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f'<h1> Blog {blog_id}! </h1>'


if __name__ == '__main__':
    app.run(debug=True)
