from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_word():
    return render_template('index.html', content='Test!!!', cars=['BMW', 'Test', 'Motor'])


if __name__ == '__main__':
    app.run(debug=True)
