import socket
import requests

# global variables
PORT = 105

def get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def test_decision_endpoint_returns_okay_status():
    url = "http://{}:{}/decision/".format(get_local_ip_address(), PORT)
    state_data = {"user_id": "test_user", "prior_day_brush_duration": 240, \
    "time_of_day": 0, "day_type": 0, "app_engagement": 1}
    r = requests.post(url, json=state_data)
    assert r.status_code == 200

test_decision_endpoint_returns_okay_status()
print("All Tests Passed.")
