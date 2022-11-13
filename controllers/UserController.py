from flask import request

def index():
    return "Hello"

def signup():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    return username + password