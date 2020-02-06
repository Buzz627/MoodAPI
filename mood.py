import pymongo

client=pymongo.MongoClient()
db = client.moodAPI
collection=db.moods

def saveMood(data):
	collection.insert_one(data)

