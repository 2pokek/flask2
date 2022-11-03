from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db,Reviews


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3.db'

db.init_app(app)

@app.route('/')
def main_page():
        return render_template('main_page.html')

@app.route('/pricing')
def pricing_page():
        return render_template('pricing.html')

@app.route('/about')
def about_page():
        return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

