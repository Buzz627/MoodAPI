from flask import Flask, jsonify, request
# from flask_api import status
from datetime import datetime
import json
from mood import saveMood, getMood


app = Flask(__name__)


@app.route("/mood", methods=['POST'])
def mood():
	data = request.json
	if "user" not in data:
		return jsonify({"message": "user in needed"}), 400
	if "mood" not in data:
		return jsonify({"message": "mood in needed"}), 400
	saveMood({"mood": data["mood"], "user":data["user"], "time": datetime.now()})
	return jsonify(), 200


@app.route("/mood", methods=['GET'])
def showMood():
	data=getMood("buzz")
	print("here", data)
	result=data[0]
	del result["_id"]
	return jsonify(result)
