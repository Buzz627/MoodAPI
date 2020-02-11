from flask import Flask, jsonify, request, abort
# from flask_api import status
from datetime import datetime
import json
from mood import *


app = Flask(__name__)
# app.run(host="0.0.0.0", port=5000)
# app.run()


@app.route("/mood", methods=['POST'])
def mood():
	data = request.json
	if "user" not in data:
		abort(400)
		# return jsonify({"message": "user in needed"}), 400

	if "mood" not in data:
		abort(400)
		# return jsonify({"message": "mood in needed"}), 400

	saveMood({"mood": data["mood"], "user":data["user"], "time": datetime.datetime.now()})
	return jsonify(), 200


@app.route("/mood", methods=['GET'])
def showMood():
	jsonBody=request.json
	data=getMood(jsonBody["user"])
	print("here", data)
	result=data[0]
	del result["_id"]
	result["streak"]=getStreak(jsonBody["user"])
	percentile=getPercentile(jsonBody["user"])
	if percentile>=0.5:
		result["percentile"]=percentile*100
	return jsonify(result)



if __name__=="__main__":
	print(datetime.fromtimestamp(1581009183))