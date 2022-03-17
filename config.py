# user = 'root'
# password = '1234'
# host='127.0.0.1'
# port = '3305'
# database = 'sample'
# mysql_engine = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
# user, password, host, port, database)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1:3305/sample'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY = "flask-app-secret"
# JWT_SECRET_KEY = "aaa-bbb-ccc"
# db=SQLAlchemy()
# db.init_app(app)
# @app.before_first_request
# def initialize_database():
#     print('step2')
#     db.create_all()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1:3305/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy()


db.init_app(app)


@app.before_first_request
def initialize_database():
    print('step2')
    db.create_all()