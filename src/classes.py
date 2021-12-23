import os
import sys
import json

from flask import request
from app import app
from util import create_response
from settings import APP_STATIC

try:
    with open(os.path.join(APP_STATIC, 'class_data.json'),'r') as filedata:
            CLASS_DATA = json.load(filedata)
    with open(os.path.join(APP_STATIC,'class_data_previous.json'),'r') as filedata:
            PREVIOUS_CLASS_DATA = json.load(filedata)
except Exception as e:
    print('Error loading json data: '+ str(e), file=sys.stderr)
    CLASS_DATA = {}
    PREVIOUS_CLASS_DATA = {}

@app.route('/api/react/students/5022025924/classes/completed/',methods=['GET'])
def get_completed():
    return create_response(PREVIOUS_CLASS_DATA,200,origin='*')

@app.route('/api/react/classes/',methods=['GET'])
def get_classes():
    return create_response(CLASS_DATA,200,'*')