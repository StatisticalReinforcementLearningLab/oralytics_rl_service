# Reinforcement Learning Algorithm for the Oralytics Study
Backend service for the RL Algorithm for Oralytics

## Local Development
To test locally, you need to install and set up Flask. [Here](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24) is an article on quick setup.

### Testing Endpoints Locally
To test the endpoints, go to the terminal and type `python3 endpoints.py` in the endpoints folder. You should see something like this:

`* Running on http://0.0.0.0:105/ (Press CTRL+C to quit)`

Note that `0.0.0.0` will be replaced by your unique local IP address.

Examples of how to call the endpoints (Ref: [Endpoints Unit Testing](https://github.com/StatisticalReinforcementLearningLab/oralytics_rl_service/blob/main/testing/endpoints_test.py)):

To call the decision time endpoint:
Make a post request `r = requests.post(url, json=json_data)` where `url` is `http://{YOUR_LOCAL_IP_ADDRESS}:{PORT=105}/decision/` and `json_data` is a JSON struct of state values.

To call the update time endpoint:

`http://0.0.0.0:105/update/`
