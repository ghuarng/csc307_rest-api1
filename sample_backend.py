from flask import Flask
app = Flask(__name__)

users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name' : 'Charlie',
            'job' : 'Janitor',
        }, 
        {
            'id' : 'abc123', 
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222', 
            'name': 'Mac',
            'job': 'Professor',
        }, 
        {
            'id' : 'yat999', 
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555', 
            'name': 'Dennis',
            'job': 'Bartender',
        }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/users')
def get_users():
    return users