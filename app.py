import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
app=Flask(__name__)
from config import *

class User(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.String(45), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

class todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, nullable=False)
    text=db.Column(db.String(100), nullable=False)
    complete=db.Column(db.Boolean)

    def save(self):
        db.session.add(self)
        db.session.commit()

@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output=[]
    # print(users)
    for user in users:
        user_data={}
        # print(user.public_id)
        user_data['public_id']=user.public_id
        user_data['name']=user.name
        user_data['password']=user.password
        user_data['admin']=user.admin
        output.append(user_data)
        print(user_data)
    return jsonify({'users':output})

@app.route('/user/<user_id>', methods=['GET'])
def get_one_users():
    return ""

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    password_hash = generate_password_hash(data["password"], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()),name=data['name'], password=password_hash, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" : "new user created"})

@app.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ""

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return " "

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1", port=8000)