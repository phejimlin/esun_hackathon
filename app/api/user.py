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
		except (ValueError, KeyError, TypeError) as error:
			raise InvalidUsage("Missing Parameters: " + str(error))

		if User.register(ssn, password, name, email):
			return ("Sign up successfully!", 200)
		else:
			return ("The account already Signup!", 200)