from ..models import User
from ..models import Feedback
from ..invalidusage import InvalidUsage
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask.json import jsonify


def register():
	json_dict = request.get_json()
	if json_dict is None:
		raise InvalidUsage("Mimetype is not application/json!")
	else:
		try:
			ssn = json_dict['ssn']
			password = json_dict['password']
			name = json_dict['name']
			email = json_dict['email']
			age = json_dict['age']
			education_level = json_dict['education_level']
			occupation = json_dict['occupation']
			annual_income = json_dict['annual_income']
			employment_year = json_dict['employment_year']
			resident_status=json_dict['resident_status']
			credit_card_status=json_dict['credit_card_status']
			limit_amount=json_dict['limit_amount']
			pre_owned_status=json_dict['pre_owned_status']
			revolving_count=json_dict['revolving_count']
			revolving_amount=json_dict['revolving_amount']
			debt_status=json_dict['debt_status']
			mortgage=json_dict['mortgage']
			debt_amount=json_dict['debt_amount']
			balance_amount=json_dict['balance_amount']
			debt=json_dict['debt']
			delinquent=json_dict['delinquent']
			ever_in_use=json_dict['ever_in_use']
			
		except (ValueError, KeyError, TypeError) as error:
			raise InvalidUsage("Missing Parameters:" + str(error))

		if User.register(
			ssn, password, name, email,
			education_level, occupation, age, annual_income, employment_year, resident_status, credit_card_status, limit_amount,
			pre_owned_status, revolving_count, revolving_amount, debt_status, mortgage, debt_amount, balance_amount, debt, delinquent, ever_in_use
		):
			session['ssn'] = ssn
			return ("Sign up successfully!", 200)
		else:
			return ("The account already Signup!", 200)

def login():
	json_dict = request.get_json()
	if json_dict is None:
		raise InvalidUsage("Mimetype is not application/json!")
	else:
		try:
			ssn = json_dict['ssn']
			password = json_dict['password']
		except (ValueError, KeyError, TypeError) as error:
			raise InvalidUsage("Missing Parameters:" + str(error))

		if User.login(ssn, password):
			session['ssn'] = ssn
			return ("Login successfully!", 200)
		else:
			return ("Login Error!", 200)

def get_profile():
	ssn = session['ssn']
	other_ssn = request.args.get('name')
	if other_ssn is None:
		return jsonify(User.get_user_info(ssn))
	else:
		other_user = User.get_user_info(ssn, other_ssn)
		if other_user:
			return jsonify(other_user)
		else:
			return ("Not found", 404)
