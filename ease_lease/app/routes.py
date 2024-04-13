from flask import render_template, request, jsonify
from app.utils import is_valid_login, is_username_available, create_new_user, get_user_id, get_user_info
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if is_valid_login(username, password):
        user_id = get_user_id(username, password)
        return jsonify({'success': True, 'user_id': user_id})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    phone_number = request.json.get('phone_number')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    if is_username_available(username):
        create_new_user(username, password, phone_number, first_name, last_name)
        user_id = get_user_id(username, password)
        return jsonify({'success': True, 'user_id': user_id})
    else:
        return jsonify({'success': False, 'message': 'Username already exists'})

@app.route('/listings/<int:user_id>', methods=['GET'])
def listings(user_id):
    user_info = get_user_info(user_id)
    print(user_info)
    return render_template('listings.html', user = user_info)
