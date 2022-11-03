from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30),default='Unknown')
    #mark = db.comlumn(db.Integer(1-5))
    text=db.Column(db.String(500),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return '<Reviews %r' % self.id
