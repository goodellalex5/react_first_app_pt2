from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


users = {
    'users_list':
        [
            {
                'id': 'xyz789',
                'name': 'Charlie',
                'job': 'Janitor',
            },
            {
                'id': 'abc123',
                'name': 'Mac',
                'job': 'Bouncer',
            },
            {
                'id': 'ppp222',
                'name': 'Mac',
                'job': 'Professor',
            },
            {
                'id': 'yat999',
                'name': 'Dee',
                'job': 'Aspring actress',
            },
            {
                'id': 'zap555',
                'name': 'Dennis',
                'job': 'Bartender',
            }
        ]
}


@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        new_id = random.randint(0, 1000000)
        full = userToAdd.update({'id':new_id})
        print(userToAdd)
        users['users_list'].append(full)
        resp = jsonify(success=True)
        return userToAdd, 201
