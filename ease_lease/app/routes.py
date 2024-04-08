from flask import render_template, request, jsonify
from utils import is_valid_login, is_username_available, create_new_user
from app import app

@app.route('/')
def index():
    return "home page"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if is_valid_login(username, password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if is_username_available(username):
        create_new_user(username, password)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Username already exists'})