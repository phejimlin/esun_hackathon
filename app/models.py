# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db
import datetime
import uuid
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='idea2f2p4.eastasia.cloudapp.azure.com', port='8545'))
contract_address = '0x11bdefdc7179d1e8760f9ddbd70d40ae2024923d'
master_address = '0xcb3dce3b17320e5becf8a2c1ffcf329fa7e87069'
master_passphrase = '1QAZ2wsx3edc'
contract_abi = [{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"deals","outputs":[{"name":"buyer","type":"address"},{"name":"seller","type":"address"},{"name":"buyer_sent","type":"bool"},{"name":"seller_sent","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"timestamp","type":"uint256"},{"name":"addr","type":"address"},{"name":"score","type":"int256"}],"name":"set_user_score","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"dealID","type":"uint256"},{"name":"timestamp","type":"string"},{"name":"score","type":"int256"},{"name":"message","type":"string"}],"name":"send_feedback","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"timestamp","type":"string"},{"name":"itemID","type":"uint256"},{"name":"buyer","type":"address"},{"name":"seller","type":"address"}],"name":"create_deal","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"master","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"inputs":[],"payable":False,"type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"_dealID","type":"uint256"},{"indexed":False,"name":"_timestamp","type":"string"},{"indexed":False,"name":"_itemID","type":"uint256"},{"indexed":True,"name":"_buyer","type":"address"},{"indexed":True,"name":"_seller","type":"address"}],"name":"deal_created","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_dealID","type":"uint256"},{"indexed":False,"name":"_timestamp","type":"string"},{"indexed":True,"name":"sender","type":"address"},{"indexed":True,"name":"receiver","type":"address"},{"indexed":False,"name":"_sender_is_seller","type":"bool"},{"indexed":False,"name":"_score","type":"int256"},{"indexed":False,"name":"_message","type":"string"}],"name":"feedback_sent","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"addr","type":"address"},{"indexed":True,"name":"timestamp","type":"uint256"},{"indexed":False,"name":"old_score","type":"int256"},{"indexed":False,"name":"new_score","type":"int256"}],"name":"user_score_changed","type":"event"}]

class User(db.Model):
	# personalInfo
	ssn = db.Column(db.String(64), primary_key=True)
	password = db.Column(db.String(500))
	name = db.Column(db.String(500))
	email = db.Column(db.String(120), unique=True)
	# blockchain
	credit = db.Column(db.Integer)
	eth_address = db.Column(db.String(50))
	eth_password = db.Column(db.String(500))
	# esun
	education_level = db.Column(db.String(1))
	occupation = db.Column(db.String(1))
	age = db.Column(db.String(1))
	annual_income = db.Column(db.String(7))
	employment_year = db.Column(db.String(1))
	resident_status = db.Column(db.String(5))
	credit_card_status = db.Column(db.String(1))
	limit_amount = db.Column(db.String(6))
	pre_owned_status = db.Column(db.String(1))
	revolving_count = db.Column(db.String(1))
	revolving_amount = db.Column(db.String(7))
	debt_status = db.Column(db.String(1))
	mortgage = db.Column(db.String(1))
	debt_amount = db.Column(db.String(7))
	balance_amount = db.Column(db.String(7))
	debt = db.Column(db.String(1))
	delinquent = db.Column(db.String(1))
	ever_in_use = db.Column(db.String(1))


	def __init__(
		self, ssn, password, name, email,
		eth_address, eth_password,
		education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
		pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use
	):
		self.ssn = ssn
		self.password = password
		self.name = name
		self.email = email
		self.credit = 0
		self.eth_address = eth_address
		self.eth_password = eth_password
		self.education_level = education_level
		self.occupation = occupation
		self.age = age
		self.annual_income = annual_income
		self.employment_year = employment_year
		self.resident_status = resident_status
		self.credit_card_status = credit_card_status
		self.limit_amount = limit_amount
		self.pre_owned_status = pre_owned_status
		self.revolving_count = revolving_count
		self.revolving_amount = revolving_amount
		self.debt_status = debt_status
		self.mortgage = mortgage
		self.debt_amount = debt_amount
		self.balance_amount = balance_amount
		self.debt = debt
		self.delinquent = delinquent
		self.ever_in_use = ever_in_use


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.ssn)

	def __repr__(self):
		return '<User %r>' % (self.name)

	@staticmethod
	def register(
		ssn, password, name, email,
		education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
		pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use
	):
		user = User.query.get(ssn)
		if not user:
			eth_password = str(uuid.uuid1())
			eth_address = web3.personal.newAccount(eth_password)

			new_user = User(
				ssn, password, name, email, eth_address, eth_password,
				education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
				pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use
			)
			db.session.add(new_user)
			db.session.commit()
			return True
		else:
			# This account already been signup.
			return False

	@staticmethod
	def login(ssn, password):
		user = User.query.get(ssn)
		if user:
			return True
		else:
			return False
		

class Deal(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	item_id = db.column(db.Integer)
	timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	buyer_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
	seller_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))

	def __init__(id, item_id, buyer_id, seller_id):
		self.id = id
		self.item_id = item_id
		self.buyer_id = buyer_id
		self.seller_id = seller_id

	def create_deal(item_id, buyer_id, seller_id):
		# Create deal in blockchain and get deal id
		# Get buyer and seller address first
		buyer_addr = User.query.get(buyer_id).eth_address
		seller_addr = User.query.get(seller_id).eth_address

		#Unlock and call contract function
		contract = web3.eth.contract(address = contract_address, abi = contract_abi)
		web3.personal.unlockAccount(master_address, master_passphrase)
		receipt = contract.transact({'from': master_address}).create_deal(
			datetime.datetime.utcnow().strftime('%B %d %Y %H:%M:%S'), item_id, buyer_addr, seller_addr)
		



class Feedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	score = db.Column(db.Integer)
	message = db.Column(db.Text)
	from_is_seller = db.Column(db.Boolean)
	created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	from_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
	from_who = db.relationship('User', foreign_keys=[from_user_id])
	to_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
	to_who = db.relationship('User', foreign_keys=[to_user_id])

	def __init__(self, score, message, from_who, to_who, from_is_seller, created_date=None):
		self.score = score
		self.message = message
		self.from_is_seller = from_is_seller
		if created_date is None:
			created_date = datetime.datetime.utcnow()
		self.from_who = from_who
		self.from_user_id = from_who.ssn
		self.to_who = to_who
		self.to_user_id = to_who.ssn

	def __repr__(self):
		return '<Feedback %r>' % (self.message)
