import pymongo
import datetime

# client=pymongo.MongoClient()
client=pymongo.MongoClient("mongodb://mongo:27018")
db = client.moodAPI
collection=db.moods

def saveMood(data):
	collection.insert_one(data)

def getMood(user):
	data=collection.find({"user":user}, collation={"locale":"en", "strength":2}, sort=[("time", -1)])
	return list(data)

def getStreak(user):
	data=collection.find({"user":user}, {"time":1}, collation={"locale":"en", "strength":2}, sort=[("time", -1)])
	start=data.next()["time"]
	streak=0
	for i in range(data.count()-1):
		end=data.next()["time"]
		if start.date()-end.date()==datetime.timedelta(1):
			streak+=1
		elif start.date()-end.date()==datetime.timedelta(0):
			pass
		else:
			break
		
		start=end

	return streak+1

def longestStreak(user):
	data=collection.find({"user":user}, {"time":1}, collation={"locale":"en", "strength":2}, sort=[("time", -1)])
	start=data.next()["time"]
	streak=[]
	curStreak=0
	for i in range(data.count()-1):

		end=data.next()["time"]
		if start.date()-end.date()==datetime.timedelta(1):

			curStreak+=1
		elif start.date()-end.date()==datetime.timedelta(0):
			pass
		else:
			streak.append(curStreak+1)
			curStreak=0
		
		start=end
	else:
		streak.append(curStreak+1)

	return max(streak)


def getPercentile(user):
	bestStreak=longestStreak(user)
	names=collection.distinct("user", {})
	streaks=[]
	for name in names:
		if name.lower()==user.lower():
			continue

		streaks.append(longestStreak(name))
	less=sum(list(map(lambda x: x<bestStreak, streaks)))
	return less/(len(streaks)+1)


if __name__=="__main__":
	print(getPercentile("buzz"))

