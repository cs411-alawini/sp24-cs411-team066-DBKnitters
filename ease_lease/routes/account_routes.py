from flask import render_template, request, jsonify, session
from utils.account_utils import is_valid_login, is_username_available, create_new_user, get_user_id, get_user_info
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    login_type = request.json.get('login_type')
    if is_valid_login(username, password):
        user_id = get_user_id(username, password)
        user_info = get_user_info(user_id)
        session['user_name'] = user_info['user_name']
        session['phone_number'] = user_info['phone_number']
        session['user_id'] = user_id
        session['login_type'] = login_type
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
        session['user_id'] = user_id
        session['login_type'] = 'tenant'
        return jsonify({'success': True, 'user_id': user_id})
    else:
        return jsonify({'success': False, 'message': 'Username already exists'})
