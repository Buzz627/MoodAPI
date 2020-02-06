from flask import Flask, jsonify, request
# from flask_api import status
from datetime import datetime
import json
from mood import saveMood


app = Flask(__name__)


@app.route("/mood", methods=['POST'])
def mood():
	data = request.json
	if "user" not in data:
		return jsonify({"message": "user in needed"}), 400
	if "mood" not in data:
		return jsonify({"message": "mood in needed"}), 400
	print({"mood": data["mood"], "user":data["user"], "time": datetime.now()})
	return jsonify(), 200



