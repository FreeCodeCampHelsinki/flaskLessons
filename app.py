from flask import Flask
from users import users
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/company"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(users) 

class People(db.Model):
    people_id = db.Column(db.Integer,primary_key=True)
    people_name = db.Column(db.Unicode(80))
    people_email = db.Column(db.String(255),unique=True)
    people_created = db.Column(db.DateTime,nullable=True)

    def __init__(self,name,email):
        self.people_name = name
        self.people_email = email

# db.create_all()
# new_user = People('Umer','umer@mydomain.com')
# db.session.add(new_user)
# db.session.commit()

results = db.engine.execute("SELECT * FROM people")

for person in results:
    print(person['people_name'])
