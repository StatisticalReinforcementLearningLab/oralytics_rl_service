from flask import Flask, request
from process_state import *
from action_selection import *

app = Flask(__name__)
@app.route('/decision/', methods=['GET', 'POST'])
def decision():
    state_data = request.get_json()
    current_state = process_state(state_data)
    action_schedule = action_selection(state_data['user_id'], current_state)
    # 1. main controller will send current state features as a JSON string
    # 2. we will convert the JSON string to a dictionary of values
    return action_schedule

@app.route('/update/', methods=['GET'])
def update():
    # 1. goes to main controller data base and grab updated batch data for users
    # 2. calls internal posterior update function to update parameters for algorithm
    return "Update Time Endpoint Works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
