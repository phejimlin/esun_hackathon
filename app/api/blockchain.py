from ..models import Blockchain
from ..invalidusage import InvalidUsage
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask.json import jsonify
from ..models import web3

def get_newest_20_blocks():
	return jsonify(Blockchain.get_newest_20_blocks())

def query_block_chain():
	query = request.args.get('query')
	if '0x' in query:
		# find transaction
		result = web3.eth.getTransaction(query)
		print(result)
		if result:
			result['type'] = 'transaction'
			return jsonify(result)
		else:
			return ("Not found", 404)
	else:
		# find block
		result = web3.eth.getBlock(int(query))
		print(result)
		if result:
			result['type'] = 'block'
			return jsonify(result)
		else:
			return ("Not found", 404)
