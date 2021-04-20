from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

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

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_userjob = request.args.get('job')

        if search_username and not search_userjob:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)

            return subdict
        
        elif search_username and search_userjob:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_userjob:
                    subdict['users_list'].append(user)
            
            return subdict
    
        return users
    
    elif request.method == 'POST':
        userToAdd = request.get_json()

        #Generate id
        user_id = ''
        for i in range(3):
            rand_letter = random.choice(string.ascii_letters).lower()
            user_id += rand_letter
        for i in range(3):
            user_id += str(random.randint(0,9))
        
        #Add id to user
        userToAdd['id'] = user_id

        #Insert new user
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        resp.status_code = 201
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return({})
    
        return users
    
    elif request.method == 'DELETE':
        if id:
            resp = jsonify("User " + id + " not found")
            resp.status_code = 404

            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify("User " + id + " deleted")
                    resp.status_code = 204

            return resp