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


@app.route('/test/')
def test():
	web3 = Web3(KeepAliveRPCProvider(host='idea2f2p4.eastasia.cloudapp.azure.com', port='8545'))
	balance = web3.eth.getBalance('0xcb3dce3b17320e5becf8a2c1ffcf329fa7e87069')
	print(balance)
	# print(web3.personal.newAccount('1234'))
	print(web3.eth.accounts)
	return str(balance)


@app.route('/list/')
def posts():
	return render_template('list.html')

@app.route('/new/')
@login_required
def new():
	form = ExampleForm()
	return render_template('new.html', form=form)

@app.route('/save/', methods=['GET','POST'])
@login_required
def save():
	form = ExampleForm()
	if form.validate_on_submit():
		print("salvando os dados:")
		print(form.title.data)
		print(form.content.data)
		print(form.date.data)
		flash('Dados salvos!')
	return render_template('new.html', form=form)

@app.route('/view/<id>/')
def view(id):
	return render_template('view.html')


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
	# if request.method == 'POST':
	# 	return member.register()
	if 'id' in session:
		return redirect(url_for('main'))
	else:
		return render_template('login.html')

# === User login methods ===

@app.before_request
def before_request():
	g.user = current_user

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
# 	print(g.user)
# 	if g.user is not None and g.user.is_authenticated:
# 		return redirect(url_for('index'))
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		login_user(g.user)

# 	return render_template('login.html', title='Sign In', form=form)

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

