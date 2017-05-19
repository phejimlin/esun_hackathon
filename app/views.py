# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, session, send_from_directory
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from .forms import LoginForm, ExampleForm
from .invalidusage import InvalidUsage
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from .api import user
from flask.json import jsonify

# serving static file such as js css.
@app.route('/<path:filename>')
def send_static(filename):
    return send_from_directory('templates', filename)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/list/')
def posts():
	return render_template('list.html')


@app.route('/profile/', methods=['GET'])
def profile():
	return render_template('profile.html')


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		return user.register()
	else:
		return render_template('register.html')

		
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return user.login()
	if 'ssn' in session:
		return redirect(url_for('profile'))
	else:
		return render_template('login.html')

# === User login methods ===

@app.before_request
def before_request():
	g.user = current_user

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))


@app.route('/logout/')
def logout():
	logout_user()
	return redirect(url_for('index'))
# ====================

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
	if error.get_error_type() == 'redirectToLoginPage':
		return redirect(url_for('login'))
	else:
		response = jsonify(error.to_dict())
		response.status_code = error.status_code
		return response
