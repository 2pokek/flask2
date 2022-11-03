from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Reviews

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3.db'

db.init_app(app)


@app.route('/create')
def create():
    db.create_all()
    return 'all tables created'


@app.route('/')
def main_page():
    reviews = Reviews.query.order_by(Reviews.date.desc()).all()
    return render_template("main_page.html", reviews=reviews)


@app.route('/pricing')
def pricing_page():
    reviews = Reviews.query.order_by(Reviews.date.desc()).all()
    return render_template("pricing.html", reviews=reviews)


@app.route('/about')
def about_page():
    reviews = Reviews.query.order_by(Reviews.date.desc()).all()
    return render_template("about.html", reviews=reviews)


@app.route('/create_comment', methods=['POST', 'GET'])
def create_comment():
    if request.method == "POST":
        nickname = request.form['nickname']
        text = request.form['text']

        review = Reviews(nickname=nickname, text=text)

        try:
            db.session.add(review)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error, try again later'
    else:
        return render_template("create_comment.html")



@app.route('/reviews/<int:id>/update', methods=['POST', 'GET'])
def comment_update(id):
    review = Reviews.query.get(id)
    if request.method == "POST":
        review.nickname = request.form['nickname']
        review.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error, try again later'
    else:
        review = Reviews.query.get(id)
        return render_template("update_comment.html", review=review)


@app.route('/reviews/<int:id>/delete')
def comment_delete(id):
    review = Reviews.query.get_or_404(id)

    try:
        db.session.delete(review)
        db.session.commit()
        return redirect('/')
    except:
        return "Error while deleting"
    return render_template("comment.html", review=review)


if __name__ == '__main__':
    app.run(debug=True)
