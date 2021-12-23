#!/usr/bin/env python
from flask import Flask, request, jsonify, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import os
import uuid
from werkzeug.security import generate_password_hash
from dateutil.parser import parse as date_parse
from dateutil.tz import gettz
import datetime


from app import app
from tables import *
from activities import *
from applications import *
from categories import *
from classes import *
from database import db
from foodarchetypes import *
from foods import *
from meals import *
from messages import *
from models import *
from orders import *
from products import *
from reviews import *
from tables import *
from tags import *
from users import *
from util import *

tzinfo = gettz('America/Chicago')



def delete_empty_string_user():
    users = User.query.filter_by(username='').all()
    for user in users:
        db.session.delete(user)
    db.session.commit()


@app.route('/cards/',methods=['GET'])
def get_cards():
    return create_response(CARD_DATA,200,'*')

@app.route('/')
def index():
    return create_response({'message':'Nothing here!'},200,'*')

@app.route('/teapot')
def teapot():
    return create_response({'message':"I'm a teapot"},418,'*')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
