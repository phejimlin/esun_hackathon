# from ..models import User
from ..models import Deal
from ..models import Feedback
from ..invalidusage import InvalidUsage
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask.json import jsonify

def create_deal():
	json_dict = request.get_json()
	if json_dict is None:
		raise InvalidUsage("Mimetype is not application/json!")
	else:
		try:
			item_id = json_dict['item_id']
			buyer_id = json_dict['buyer_id']
			seller_id = json_dict['seller_id']
		except (ValueError, KeyError, TypeError) as error:
			raise InvalidUsage("Missing Parameters: " + str(error))
		tx_hash = Deal.create_deal(item_id, buyer_id, seller_id)
		if tx_hash:
			return ("Deal is sent to blockchain, transaction hash: " + tx_hash, 200)
		else:
			return ("The account already Signup!", 200)