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
		tx_hash = Feedback.create_feedback(deal_id, score, message, from_user_id, to_user_id)
		if tx_hash:
			return ("Feedback is sent to blockchain, transaction hash: " + tx_hash, 200)
		else:
			return ("Failed to add feedback", 400)

def get_all_received_feedback():
	ssn = session['ssn']
	other_name = request.args.get('name')
	if other_name is None:
		return jsonify(Feedback.get_all_received_feedback(ssn))
	else:
		comments = Feedback.get_all_received_feedback(ssn, other_name)
		if comments is None:
			return("Not found", 404)
		return jsonify(comments)

def get_received_feedback_from_buyer():
	ssn = session['ssn']
	other_name = request.args.get('name')
	if other_name is None:
		return jsonify(Feedback.get_received_feedback_from_buyer(ssn))
	else:
		comments = Feedback.get_received_feedback_from_buyer(ssn, other_name)
		if comments is None:
			return("Not found", 404)
		return jsonify(comments)

def get_received_feedback_from_seller():
	ssn = session['ssn']
	other_name = request.args.get('name')
	if other_name is None:
		return jsonify(Feedback.get_received_feedback_from_seller(ssn))
	else:
		comments = Feedback.get_received_feedback_from_seller(ssn, other_name)
		if comments is None:
			return("Not found", 404)
		return jsonify(comments)

def get_all_sent_feedback():
	ssn = session['ssn']
	other_name = request.args.get('name')
	if other_name is None:
		return jsonify(Feedback.get_all_sent_feedback(ssn))
	else:
		comments = Feedback.get_all_sent_feedback(ssn, other_name)
		if comments is None:
			return("Not found", 404)
		return jsonify(comments)