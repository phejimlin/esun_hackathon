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

class User(db.Model):
	ssn = db.Column(db.String(64), primary_key=True)
	password = db.Column(db.String(500))
	name = db.Column(db.String(500))
	email = db.Column(db.String(120), unique=True)
	credit = db.Column(db.Integer)
	eth_address = db.Column(db.String(50))
	eth_password = db.Column(db.String(500))


	def __init__(self, ssn, password, name, email, eth_address, eth_password):
		self.ssn = ssn
		self.password = password
		self.name = name
		self.email = email
		self.credit = 0
		self.eth_address = eth_address
		self.eth_password = eth_password

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
	def register(ssn, password, name, email):
		user = User.query.filter_by(ssn=ssn).first()
		if not user:
			eth_password = str(uuid.uuid1())
			eth_address = web3.personal.newAccount(eth_password)

			new_user = User(ssn, password, name, email, eth_address, eth_password)
			db.session.add(new_user)
			db.session.commit()
			return True
		else:
			# This account already been signup.
			return False


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
