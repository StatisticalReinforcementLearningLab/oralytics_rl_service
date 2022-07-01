from flask import Flask
from flask import request
import numpy as np

app = Flask(__name__)
@app.route('/decision/<int:a>/', methods=['GET', 'POST'])
def decision(a):
    # 1. main controller will send current state features as a JSON string
    # 2. we will convert the JSON string to a dictionary of values
    return "Decision Time Endpoint Works with value {}!".format(a)

@app.route('/update/', methods=['GET'])
def update():
    # 1. goes to main controller data base and grab updated batch data for users
    # 2. calls internal posterior update function to update parameters for algorithm
    return "Update Time Endpoint Works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
