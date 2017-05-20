from ..models import Blockchain
from ..invalidusage import InvalidUsage
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask.json import jsonify

def get_newest_20_blocks():
	return jsonify(Blockchain.get_newest_20_blocks())
