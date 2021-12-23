from flask import request
from app import app
from util import create_response
import datetime
from faker import Faker
import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)
Faker.seed(0) 

ERROR_MESSAGE = "Oops! Something went wrong. Check to make sure that you are sending a valid request. Your received request is provided below. If it is empty, then it was most likely not provided or malformed. If you have verified that your request is valid, please contact a CS571 administrator."

def construct_request(request):
    """
    Return a request dict based on the raw Request object.
    """
    return {
        "method": request.method,
        "endpoint": request.endpoint,
        "headers": dict(request.headers),
        "data": request.get_data(as_text=True),
        "args": request.args,
    }

def generate_order():
    """
    Returns a fake order object.
    """
    order = {
        "date": fake.past_datetime().strftime("%m/%d/%Y, %H:%M:%S %p"),
        "productName": fake.ecommerce_name(),
        "amount": fake.bothify("###.##")
    }

    return order

@app.route('/api/badgershop/orders/',methods=['GET'])
def get_orders():
    amount = request.args.get('amount', None, type=int)
    orders = []

    if amount is None:
        # amount parameter is not provided
        return create_response({
            'error-msg': ERROR_MESSAGE,
            'error-req': construct_request(request),
            'date-time':  datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S %p")
            }, 400, '*')

    if amount < 0 or amount > 25:
        # amount is out of range 
        return create_response([], 200, '*')

    for _ in range(amount):
        order = generate_order()
        orders.append(order)

    return create_response(orders, 200, '*')

@app.route('/api/badgershop/order/',methods=['GET'])
def get_order():
    order = generate_order()
    
    return create_response(order, 200, '*')