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
from .api import user, deal, feedback, blockchain
from flask.json import jsonify

# serving static file such as js css.
@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    if 'ssn' in session:
        return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))

@app.route('/index', methods=['GET'])
def main():
    session_check('render_page')
    return render_template('index.html')


@app.route('/list/')
def posts():
	return render_template('list.html')


@app.route('/api/profile/', methods=['GET'])
def profile():
	session_check('render_page')
	return user.get_profile()


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
		return redirect(url_for('index'))
	else:
		return render_template('login.html')

@app.route('/blockchain/', methods=['GET'])
def blockchain_explorer():
	return render_template('blockchain.html')

@app.route('/api/blockchain/query/', methods=['GET'])
def blockchain_query():
	return blockchain.query_block_chain()

@app.route('/api/deal/', methods=['GET', 'POST'])
def deal_api():
	if request.method == 'POST':
		return deal.create_deal();

@app.route('/api/feedback/', methods=['GET', 'POST'])
def feedback_api():
	if request.method == 'POST':
		return feedback.create_feedback();

@app.route('/api/blockchain/<path:path>', methods=['GET', 'POST'])
def blockchain_api(path):
	if request.method == 'GET':
		if path == 'blocks':
			return blockchain.get_newest_20_blocks();


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


def session_check(request_type):
    # request_type only will be api or render_page.
    if request_type == 'api':
        if 'ssn' not in session:
            raise InvalidUsage("unauthorized", 401)
    elif request_type == 'render_page':
        if 'ssn' not in session:
            raise InvalidUsage(None, None, None, "redirectToLoginPage")
