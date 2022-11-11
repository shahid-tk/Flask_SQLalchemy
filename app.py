import os
from datetime import datetime
from flask import Flask
from flask-SQLAlchemy import SQLalchemy
from sqlalchemy.sql import func
 
 basedir = os.path.abspath(os.path.dirname(__file__))
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLalchemy(app)
 
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
 
@app.route('/<name>')
def home(name):
    table = Table(name=name)
    db.session.add(table)
    db.session.commit()
    return '<h1> Name Added: {name} </h1>'
 
if __name__ == '__main__':
    app.run(debug=True)
