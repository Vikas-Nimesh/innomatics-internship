# importing library
from flask import Flask

users = ['dhruv-dixit', 'azhaku', 'soham-jondhale', 'gaikwadpallavi']

# object creation
app = Flask(__name__)

# creating routes

@app.route('/')
def homepage():
    return "This is home page"

@app.route('/about')
def about_us():
    return 'This is About us page!'

@app.route("/users/<user_name>")
def verify(user_name):
    if user_name in users:
        return "Welcome {}!".format(user_name)
    
    return "Please Register."

# app run
if __name__ == "__main__":
    app.run(debug=True)
