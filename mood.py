import pymongo

client=pymongo.MongoClient()
db = client.moodAPI
collection=db.moods

def saveMood(data):
	collection.insert_one(data)

def getMood(user):
	data=collection.find({"user":user}, collation={"locale":"en", "strength":2}, sort=[("time", -1)])
	return list(data)