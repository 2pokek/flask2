from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route('/')
def main_page():
        return render_template('main_page.html')


if __name__ == '__main__':
    app.run(debug=True)

