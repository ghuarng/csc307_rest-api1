from flask import Flask
from flask import request
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
    search_username = request.args.get('name')

    if search_username:
        subdict ={'users_list' : []}
        for user in users['users_list']:
            if user['name'] == search_username:
                subdict['users_list'].append(user)

        return subdict
    
    return users

@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return({})
    
    return users