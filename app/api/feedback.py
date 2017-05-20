# from ..models import User
from ..models import Deal
from ..models import Feedback
from ..invalidusage import InvalidUsage
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask.json import jsonify

def create_feedback():
	json_dict = request.get_json()
	if json_dict is None:
		raise InvalidUsage("Mimetype is not application/json!")
	else:
		try:
			deal_id = json_dict['deal_id']
			score = json_dict['score']
			message = json_dict['message']
			from_user_id = json_dict['from_user_id']
			to_user_id = json_dict['to_user_id']
		except (ValueError, KeyError, TypeError) as error:
			raise InvalidUsage("Missing Parameters: " + str(error))
		tx_hash = Feedback.create_feedback(deal_id, score, messgae, from_user_id, to_user_id)
		if tx_hash:
			return ("Feedback is sent to blockchain, transaction hash: " + tx_hash, 200)
		else:
			return ("Failed to add feedback", 400)