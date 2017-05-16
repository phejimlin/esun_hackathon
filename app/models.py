# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db
import datetime


class User(db.Model):
	ssn = db.Column(db.String(64), primary_key=True)
	password = db.Column(db.String(500))
	name = db.Column(db.String(500))
	email = db.Column(db.String(120), unique=True)

	def __init__(self, ssn, name, email):
		self.ssn = ssn
		self.name = name
		self.email = email

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


class Feedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	score = db.Column(db.Integer)
	message = db.Column(db.Text)
	created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	from_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
	from_who = db.relationship('User', foreign_keys=[from_user_id])
	to_user_id = db.Column(db.String(64), db.ForeignKey('user.ssn'))
	to_who = db.relationship('User', foreign_keys=[to_user_id])

	def __init__(self, score, message, from_who, to_who, created_date=None):
		self.score = score
		self.message = message
		if created_date is None:
			created_date = datetime.datetime.utcnow()
		self.from_who = from_who
		self.from_user_id = from_who.ssn
		self.to_who = to_who
		self.to_user_id = to_who.ssn

	def __repr__(self):
		return '<Feedback %r>' % (self.message)
