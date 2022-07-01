# Reinforcement Learning Algorithm for the Oralytics Study
Backend service for the RL Algorithm for Oralytics

## Local Development
To test locally, you need to install and set up Flask. [Here](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24) is an article on quick setup.

### Testing Endpoints Locally
To test the endpoints, go to the terminal and type `python3 endpoints.py` in the endpoints folder. You should see something like this:

`* Running on http://0.0.0.0:105/ (Press CTRL+C to quit)`

Then launch any web broswer and go to whichever url specified above with the added endpoint name. For example:

To call the decision time endpoint:

`http://0.0.0.0:105/decision/{SOME_INTEGER_VALUE}`

To call the update time endpoint:

`http://0.0.0.0:105/update/`
